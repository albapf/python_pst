#!/usr/bin/python3
# -*- coding: utf-8 -*-


import unittest
from app.enemy import *

class TddInPythonExample(unittest.TestCase):

    def test_enemy(self):
        e = Enemy(0,0)
        self.assertEqual(e.hp, 0)
        self.assertEqual(e.dmg, 0)
        self.assertFalse(e.is_alive())

    def test_partialexam(self):
        pe = PartialExam()
        self.assertEqual(pe.hp, 25)
        self.assertEqual(pe.dmg, 9)
        self.assertTrue(pe.is_alive())        

    def test_finalexam(self):
        fe = FinalExam()
        self.assertEqual(fe.hp, 40)
        self.assertEqual(fe.dmg, 12)
        self.assertTrue(fe.is_alive())        
        
