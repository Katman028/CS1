songs = ["Blinding lights", "As it was", "Levitating", "Flowers", "Perfect", "Anti-Hero", "Shape of you",
         "Believer", "Cruel summer", "Counting Stars"]
updated_playlist = songs[:]

print(f"number of songs {len(songs)}")
print(f"First song: {songs[0]}")
print(f"Last song: {songs[-1]} \n")
print("Opening songs")
print(songs[:3])
print("\nclosing songs")
print(songs[7:])

short_playlist = []
for i in range(0, len(songs), 2):
    short_playlist.append(songs[i])
print(f"\nshort playlist\n{short_playlist}")
updated_playlist.append("watermelon sugar")
updated_playlist.append("Save your tears")
print(f"\nupdated playlist \n{updated_playlist}")
print(f"number of songs {len(updated_playlist)}")

updated_playlist.remove("Perfect")
updated_playlist.remove("Believer")
print(f"\nplaylist after removing songs \n{updated_playlist}")

print(f"\noriginal playlist\n{songs}")

alphabetical_playlist = updated_playlist[:]
alphabetical_playlist.sort()
print(f"\nalphabetical playlist\n{alphabetical_playlist}")

lengths = [3.20, 3.47, 3.23, 4.23, 4.39, 4.21, 3.35, 3.50, 3.57, 3.05]
total_length = 0
for i in range(len(lengths)):
    total_length += lengths[i]

print(f"\ntotal playlist length {total_length}")
print(f"shortest length {min(lengths)}")
print(f"longest length {max(lengths)}")
print(f"average length {sum(lengths)/len(lengths)}")






