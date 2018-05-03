from gmusicapi import Mobileclient

def delete_dup_from_playlist(playlist):
    track_ids = set()
    deleted_count = 0

    for song in playlist:
        track_id = song['trackId']
        entry_id = song['id']
        if track_id in track_ids:
            print 'found duplicate, removing', entry_id
            api.remove_entries_from_playlist(entry_id)
            deleted_count += 1
        else:
            track_ids.add(track_id)
    if deleted_count == 0:
        print 'no duplicate found'


api = Mobileclient()
logged_in = api.login('username', 'password', '')

if __name__ == '__main__':

    if logged_in:
        playlists = api.get_all_user_playlist_contents()

        for playlist in playlists:
            print 'deleting duplicate from', playlist['name']
            delete_dup_from_playlist(playlist['tracks'])
    else:
        print 'could not sign in'
