import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    
    def setUp(self):
        self.artist = Artist("Justin", "Timberlake")
    
    # def test_task_has_description(self):
    #     self.assertEqual("Walk Dog", self.task.description)
        
        
    # def test_task_has_assignee(self):
    #     self.assertEqual("Ada Lovelace", self.task.assignee)
       
        
    # def test_task_has_duration(self):
    #     self.assertEqual(60, self.task.duration)
    
    
    # def test_task_completed_starts_false(self):
    #     self.assertEqual(False, self.task.completed)
        
    
    # def test_can_mark_test_complete(self):
    #     self.task.mark_complete()
    #     self.assertEqual(True, self.task.completed)