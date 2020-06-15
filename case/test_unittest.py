import unittest




class Test000(unittest.TestCase):

    def setUp(self) -> None:
        print('start')
    def tearDown(self) -> None:
        print('finish')
    @unittest.skipIf(False,reason='条件为假，跳不过去了')
    def test01(self):
        a=1
        b=2
        c=3
        print('1111')
        self.assertEqual(a+b,c)
    @unittest.skipUnless(3<2,reason='条件不成立，跳过')
    def test02(self):
        a=1
        b=2
        c=b-a
        print('2222')
        self.assertEqual(c,a)
if __name__ == '__main__':
    unittest.main()
