# This is Complicated.
This AutoPkg recipe to build MinecraftEdu is mostly Nick McSpadden's work. I independently devised a method for deploying that is very similar, but when he released his AutoPkg recipe, decided to switch to that.

However, there are a couple of differences. While I'm sure that Nick's rsync works flawlessly, we've been rolling with a different set of options to ensure that saved games are maintained between updates. Also, the sync can take too much time if run at every login, especially when an entire class of network-homed users simultaneously login, and the server has to start checksumming the thousands of files in Minecraft!

So my VerifyMinecraftEdu.sh script will sync the files once, based on a hidden file in the user's home. It also ignores the admin user, as I got tired of waiting for minecraft to sync every time I logged onto a classroom computer. To facilitate this, I wrote a quick text replacement processor based on work from JSSImporter to handle automatically updating the version to check for in the VerifyMinecraftEdu.sh script.

Also, Nickuses a Platypus app launcher; I stubbornly included my Automator app instead. It includes the icon.