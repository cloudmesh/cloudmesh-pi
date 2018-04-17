## How to enable the PI to 'talk' from commond line?
* Enable audio output to the analog headphone jack
```
amixer cset numid=3 1
```
* Install package to enable 'say' command
```
apt-get update
apt-get install gnustep-gui-runtim
```
* Say something fromt he command line
```
say "hello world"
```
