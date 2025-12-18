import subprocess
import


main():
  # Gets user's name 
  full_name = input("Enter user's full name (First Last): ")
  first, last = full_name.strip()

  # Creates the username
  username = f"{first.lower()}-{last.lower()}"

  print("\nSelect user role:")
  print("1: User")
  print("2: AV Tech")
  print("3: Admin")

  role = input("Enter role (1-3): ")

  if role == "1":
    role = "User"
    groups = None
  elif role == "2":
    role = "AV Tech"
    groups = "video, audio"
  elif role == "3":
    role = "Admin"
    groups = "root"

  cmd = ["useradd", "-m", "-c", full_name]
  if groups:
    cmd.append("-G")
    cmd.append(groups)
  cmd.append(username)

  subprocess.run(cmd)

  print(f"\nAccount for '{username}' has been successfully created.")

if __name__ == "__main__":
  main()
