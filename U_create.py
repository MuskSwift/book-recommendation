import pandas as pd
import shutil

# 验证用户
def validate_user(username, password):
    # 调用函数读取用户数据
    user_data = pd.read_csv('user-secret.csv', dtype={'user_name': str, 'secret': str})
    # 检查用户名和密码是否匹配
    match = user_data[(user_data['user_name'] == username) & (user_data['secret'] == password)]

    # 如果匹配项的数量大于0，则返回True，否则返回False
    return not match.empty


def register(username, password):
    # 调用函数读取用户数据
    user_data = pd.read_csv('user-secret.csv', dtype={'user_name': str, 'secret': str})

    # 创建一个新的DataFrame来存储新用户的信息
    new_user = pd.DataFrame({'user_name': [username], 'secret': [password]})

    # 将新用户的数据追加到现有的DataFrame中
    updated_user_data = pd.concat([user_data, new_user], ignore_index=True)

    # 将更新后的数据写回CSV文件，不保留索引
    updated_user_data.to_csv('user-secret.csv', index=False)

    # 源文件路径
    source_file = 'users_rating_data/sorted_user_rating.csv'
    # 目标文件路径，使用用户名作为文件名
    target_file = f'users_rating_data/{username}.csv'

    # 使用shutil库复制文件
    shutil.copy(source_file, target_file)



def check_user_exists(user_name):
    # 读取CSV文件
    df = pd.read_csv('user-secret.csv', dtype={'user_name': str, 'secret': str})

    # 检查用户名是否存在
    exists = df['user_name'].isin([user_name]).any()

    return exists

