import unittest

# 判断相等
# assertEqual(a,b)/assertNotEqual(a,b): 断言值是否相等
# assertIs(a,b)/assertIsNot(a,b): 断言是否同一对象（内存地址一样）
# assertListEqual(list1, list2)/assertItemNotEqual(list1, list2): 断言列表是否相等
# assertDictEqual(dict1, dict2)/assertDictNotEqual(dict1, dict2): 断言字典是否相等
# 是否为空
# assertIsNone(a)/assertIsNotNone(a)
# 判断真假
# assertTrue(a)/assertFalse(a)
# 是否包含
# assertIn(a,b)/assertNotIn(a,b) # b中是否包含a
# 大小判断
# assertGreater(a,b)/assertLess(a,b) : 断言a>b / 断言a<b
# assertGreaterEqual(a,b)/assertLessEqual: 断言a>=b / 断言a<=b
# 类型判断
# assertIsInstance(a,dict)/assertNotIsInstance(a,list) # 断言a为字典 / 断言a非列表

case=unittest.TestCase()#继承TestCase()
case.assertEqual(1,2.0/2) # 通过1=2.0/2   断言值是否相等
case.assertEqual(1, True) # 通过
case.assertIs(1.0, 2.0/2) # 失败，不是同一对象
case.assertListEqual([1,2],[1,2]) # 通过（顺序要一致）
case.assertDictEqual({"a":1,"b":2},{"b":2,"a":1}) # 通过，字典本无序
case.assertIsNone({}) # 失败
case.assertFalse({}) # 通过，空字典为False
case.assertIn("h","hello") # 通过
case.assertGreater(3,2) # 通过，3>2
case.assertIsInstance({"a":1}, dict) # 通过
