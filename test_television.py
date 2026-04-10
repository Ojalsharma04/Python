import pytest
import unittest
from televison import Televison

class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv_1 = Televison()

    def test_init(self):
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [0], Volume - [0]'  )

    def test_power(self):
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [0]'  )
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [0], Volume - [0]')

    def test_channel_up(self):
        self.tv_1.power()
        self.tv_1.channel_up()
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [1], Volume - [0]')
        self.tv_1.power()
        self.tv_1.channel_up()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [2], Volume - [0]')
        self.tv_1.channel_up()
        self.tv_1.channel_up()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [0]')

    def test_channel_down(self):
        self.tv_1.power()
        self.tv_1.channel_down()
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [3], Volume - [0]')
        self.tv_1.power()
        self.tv_1.channel_down()
        self.tv_1.channel_down()
        self.tv_1.channel_down()
        self.tv_1.channel_down()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [3], Volume - [0]')



    def test_volume_up(self):
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [0], Volume - [1]')
        self.tv_1.power()
        self.tv_1.volume_up()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [2]')
        self.tv_1.volume_up()
        self.tv_1.mute()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [0]')
        self.tv_1.volume_up()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [2]')

    def test_volume_down(self):
        self.tv_1.power()
        self.tv_1.volume_down()
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [0], Volume - [0]')
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.volume_up()
        self.tv_1.volume_down()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [1]')
        self.tv_1.volume_down()
        self.tv_1.mute()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [0]')
        self.tv_1.volume_down()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [0]')


    def test_mute(self):
        self.tv_1.power()
        self.tv_1.volume_up()
        self.tv_1.mute()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [0]')
        self.tv_1.mute()
        self.assertEqual(str(self.tv_1), 'Power - [True], Channel - [0], Volume - [1]')
        self.tv_1.mute()
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [0], Volume - [0]')
        self.tv_1.power()
        self.tv_1.mute()
        self.tv_1.power()
        self.assertEqual(str(self.tv_1), 'Power - [False], Channel - [0], Volume - [1]')




