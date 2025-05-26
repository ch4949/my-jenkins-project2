from main import add

def test_add():
    assert add(2, 3) == 5  # 正常情况
    #后续可修改为 assert add(2,3) == 6 触发测试失败
