from consolify_pkgs import commands
import spotipy
from consolify_pkgs.sp_module import sp


def main():
    try:
        user_profile = sp.current_user()
        print("Successfully authenticated. User profile:")
        print(f"Display name: {user_profile['display_name']}")
        print(f"User ID: {user_profile['id']}")

    except spotipy.SpotifyException as e:
        print(f"Error accessing Spotify API: {e}")
    while True:

        user_input = input("Consolify >")
        if user_input.split()[0] == "nowplaying":
            commands.nowplaying(user_input.split())
        elif user_input.split()[0] == "search":
            commands.spotify_search(user_input.split())
        elif user_input == "close":
            break
        elif user_input == "help":
            print("""===HELP===
search: Search spotify for a specific song. Use '-a' to show the album.
nowplaying: Shows the song that is playing. Use '-a' to show the album for each search result.
close: Closes the program.
            
For more info, read the README.md file.""")
        else:
            print("Not a command! Type 'help' for a list of commands.")


if __name__ == "__main__":
    main()
