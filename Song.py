class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None

  #Getter method for title attribute
  def get_title(self):
    return self.__title
    pass
  
  
  #Setter method 
  def set_title(self, title):
    
    self.__title = str(title).title()
    pass


  #Getter method for next_song attribute
  def get_next_song(self):
    return self.__next_song
    pass


  # Setter method for next_song attribute
  def set_next_song(self, next_title):
    self.__next_song = next_title
    pass


  #String of song title
  def __str__(self):
    return self.get_title()
    pass


  # String with appropriate formatting 
  def __repr__(self):
    return f"{self.get_title()} -> {self.get_next_song()}"
    pass