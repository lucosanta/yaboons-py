# YABOONS - Yet Another BOOlean Network Simulator


## Boolean Networks


### States

This sub-domain represents the current state of all nodes which belong to network.
The atomic part of this sub-domain is the State.
A State is an entity characterized by an **identificator**, which is a reference to the related *Node*, a *value*,
which represents the boolean value of the *State*. *State* and *Node* concepts have to be separated because definition 
of *Node* is related only to the structure of the network while the *State* exploits the Node identificator to 
represent Node value at a fixed instant. In order to the describing the entire BN state at a
xed instant, it has to be developed also a State aggregator called States. In this entity, all the operator which manipulates State are inserted and
all the operator that let a developer creates a custom States of the BN or a randomically generated one. For this reason, I have to outline that State and
Node need to have the same identicator. During implementation phase, a validation check in order to avoid potential error will
be inserted. During the updating of the BN, the States will create a Trajectory of the BN, which will begin with a Transient and will finish in an Attractor. 
Transient and Attractor have to be defined as aggregator of States. In fact, States entity represents the value
of all Node of the BN at a xed time t. If States are aggregated, it is possible to collect States succession during the evolution of the BN. 
Trajectory entity will encapsulate the Transient and Attractor starting from an initial state.


## Description
