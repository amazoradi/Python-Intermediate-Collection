# Define a set that contains tuples. Each tuple should contain two strings:

songs = {
  ('The Beatles', 'Yesterday'),
  ('Nickelback', 'Animals'),
  ('The Rolling Stones', 'Brown Sugar'),
  ('Portugal The Man', 'Live in the Moment'),
  ('Nickelback', 'How You Remind Me'), 
  ('Metallica', 'Master of Puppets')
}

good_songs = {f'({artist}, {title})' for (artist, title) in songs if artist != "Nickelback" }

print("death to Nickeback:", good_songs)
# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.