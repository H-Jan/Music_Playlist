from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  #This method will create Song object and adds it to playlist with parameter title
  def add_song(self, title):
    new_song = Song(title)
    new_song.next = self.__first_song
    self.__first_song = new_song
    #Essentially switch the new song to the first song in the playlist, and the first song 
    #as the new song


  def find_song(self, title):
    current_song = self.__first_song
    counter = 0
    while current_song != None:
      if current_song.get_title() == title:
        return counter
      counter += 1
      current_song = current_song.get_next_song
    return -1
    # In this, we set counter to 0 and start the first block
    # In the while loop, we loop as long as theres a song until we reach
    # end of playlist. If we find the song, we return the counter indicating its position
    # Then we continue to the next song outside the while loop while maintaining counter position
      
  def remove_song(self, title):
    current_song = self.__first_song
    last_song = None

    if self.__first_song.get_title() == title:
      self.__first_song = current_song.get_next_song()
      print(f"{current_song} has been removed")
      # Setting new value to value of playlist with song removed
      return
    
    while current_song.get_next_song != title:
      if current_song.get_next_song() == None:
        print("Error, this song does not exist")
        # In case list is empty 
        return
      current_song = current_song.get_next_song()
       #Update current song to next song
    

  def length(self):
    counter = 0 
    current_song = self.__first_song

    while current_song != None:
      counter += 1
      current_song = current_song.get_next_song
      return counter
      #Simple counter loop to iterate through playlist 
    
  def print_songs(self):
    counter = 1
    current_song = self.__first_song
    
    while current_song != none:
      counter += 1
      print(f"{counter}. {current_song}")
      current_song = current_song.get_next_song
    return
  