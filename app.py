# 导入所需的Flask模块和其他依赖
from flask import Flask, render_template, request, jsonify, redirect, url_for
# 导入SQLAlchemy用于数据库操作
from flask_sqlalchemy import SQLAlchemy
# 导入datetime用于处理时间
from datetime import datetime
# 导入pymysql用于MySQL数据库连接
import pymysql

# 将pymysql安装为MySQLdb，用于兼容性
pymysql.install_as_MySQLdb()

# 创建Flask应用实例
app = Flask(__name__)

def init_db():
    """初始化数据库的函数"""
    try:
        # 创建与MySQL的连接
        conn = pymysql.connect(
            host='localhost',  # 数据库主机地址
            user='root',      # 数据库用户名
            password='root123456'  # 数据库密码
        )
        cursor = conn.cursor()
        
        # 创建数据库，如果不存在的话，并设置字符集
        cursor.execute("CREATE DATABASE IF NOT EXISTS todo_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        conn.commit()
        
        # 关闭数据库连接
        cursor.close()
        conn.close()
        
        print("数据库初始化成功！")
    except Exception as e:
        print(f"数据库初始化错误: {str(e)}")

# 调用初始化数据库函数
init_db()

# 配置SQLAlchemy的数据库连接URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123456@localhost/todo_db'
# 关闭SQLAlchemy的修改跟踪功能，提高性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建SQLAlchemy实例
db = SQLAlchemy(app)

# 定义Todo数据模型类
class Todo(db.Model):
    __tablename__ = 'todos'  # 指定数据库表名
    
    # 定义数据库字段
    id = db.Column(db.Integer, primary_key=True)  # 主键ID
    title = db.Column(db.String(100), nullable=False)  # 待办事项标题
    completed = db.Column(db.Boolean, default=False)  # 完成状态
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # 创建时间

    def to_dict(self):
        """将Todo对象转换为字典格式"""
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# 在应用上下文中创建所有数据库表
with app.app_context():
    db.create_all()

# 首页路由
@app.route('/')
def index():
    # 获取所有待办事项，按创建时间降序排序
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template('index.html', todos=todos)

# 添加待办事项的路由
@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        # 创建新的待办事项
        new_todo = Todo(title=title)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('index'))

# 切换待办事项状态的路由
@app.route('/toggle/<int:todo_id>')
def toggle(todo_id):
    # 获取指定ID的待办事项
    todo = Todo.query.get_or_404(todo_id)
    # 切换完成状态
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

# 删除待办事项的路由
@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    # 获取并删除指定ID的待办事项
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

# API路由：获取所有待办事项
@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return jsonify([todo.to_dict() for todo in todos])

# API路由：创建新的待办事项
@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': '标题不能为空'}), 400
    
    # 创建新的待办事项
    new_todo = Todo(title=data['title'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

# API路由：更新待办事项
@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    # 获取指定ID的待办事项
    todo = Todo.query.get_or_404(todo_id)
    data = request.get_json()
    
    # 更新待办事项的属性
    if 'title' in data:
        todo.title = data['title']
    if 'completed' in data:
        todo.completed = data['completed']
    
    db.session.commit()
    return jsonify(todo.to_dict())

# API路由：删除待办事项
@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    # 获取并删除指定ID的待办事项
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return '', 204

# 程序入口
if __name__ == '__main__':
    # 以调试模式运行应用，监听5001端口
    app.run(debug=True, port=5001)