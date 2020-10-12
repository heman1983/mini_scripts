
import json

# app配置有两套环境，测试环境和线上环境，运行上线时要对线上进行校对防止缺少配置情况发生
# 我嫩公司的配置是可以通过接口返回的，这里，我们省略调用接口过程，模拟获取结果如下：

test_conf = '{"data":' \
            '[{"comment":"说明","name":"conf1","value":"配置1的值"},' \
            '{"comment":"说明","name":"conf2","value":"配置2的值"},' \
            '{"comment":"说明","name":"conf3","value":"配置3的值"}]}'

product_conf = '{"data":' \
            '[{"comment":"说明","name":"conf1","value":"配置1的值"},' \
            '{"comment":"说明","name":"conf2","value":"配置2的值"}]}'

test_data = json.loads(test_conf)['data']
product_data = json.loads(product_conf)['data']

test_set = { item['name'] for item in test_data}

product_set = { item['name'] for item in product_data}

diff_set = test_set - product_set

print(diff_set)



