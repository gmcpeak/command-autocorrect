# command-autocorrect

A neural network for correcting typos in standard Ubuntu Linux commands. This network takes as input a command--with flags and arguments--that has one or more tyos in in an attempts to determine what the user *meant* to type.

The commands that the network will be trained on are the user-level Ubuntu commands with `man` pages, found [here](http://manpages.ubuntu.com/manpages/focal/man1/).

For each command, a synthetic dataset of possible typos will be generated, each entry of which will be encoded for classification training, similarly to how it is done in this [article](https://towardsdatascience.com/deep-learning-autocorrect-product-and-technical-overview-1c219cee0698).