# API文档
模块部分使用二级header  
api接口部分使用三级header  
接口response部分默认提供两个字段code(状态码)、msg(消息)

## 用户模块

### 注册接口

* Path: accounts/myuser/signUp
* HTTP Method: POST
* URL Params: 无
* Request Headers: 无
* Request Body:  

  | 字段名称 | 必选 | 类型 | 说明 |
  |----------|-----|-----|------|
  |  email     | true  |  string | 邮箱 |
  |  username     | true  |  string | 用户名 不能超过30字符，不能有中文 |
  |  password     | true  |  string | 密码 6-16个字符 |

* Response Body: 参考示例
* 异常:

  | 状态码 | 说明 |
  |-------|------|
  |  420  | 业务逻辑错误(显示中文字符) |
  |  412  |  表单错误(显示英文字符) |

* 示例:  
```
    {
      "msg": "ok",
      "code": 200
    }
```

### 登录接口

* Path: accounts/myuser/signIn
* HTTP Method: POST
* URL Params: 无
* Request Headers: 无
* Request Body:  

  | 字段名称 | 必选 | 类型 | 说明 |
  |----------|-----|-----|------|
  |  username     | true  |  string | 用户名 |
  |  password     | true  |  string | 密码 |

* Response Body: 参考示例
* 异常:
  | 状态码 | 说明 |
  |-------|------|
  |  420  | 业务逻辑错误(显示中文字符) |
  |  412  |  表单错误(显示英文字符) |
* 示例:  
```
    {
      "msg": "ok",
      "code": 200
    }
```




