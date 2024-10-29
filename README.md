# Side Channel Attack: Timing Attack Simulation on RSA Encryption

This project demonstrates a basic RSA encryption algorithm and simulates a timing attack by introducing artificial timing variations in the decryption function. This simulation illustrates how "bad security practices" could allow timing information to leak details about the private key.

## Table of Contents
- [Introduction](#introduction)
- [Concepts](#concepts)
  - [Side Channel Attack](#side-channel-attack)
  - [RSA Encryption](#rsa-encryption)
  - [Timing Attack on RSA](#timing-attack-on-rsa)
  - [Flawed Decryption Function](#flawed-decryption-function)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Example Output](#example-output)
- [Disclaimer](#disclaimer)

## Introduction
This project aims to demonstrate how cryptographic vulnerabilities can arise through side channels, such as timing information. Here, we use Python to:
1. Implement a simple RSA encryption and decryption algorithm.
2. Introduce artificial timing variations in the decryption function to simulate a timing attack.
3. Measure and plot the decryption times to see if patterns emerge that might reveal the private key.

## Concepts

### Side Channel Attack
A **side channel attack** exploits unintentional information leaks from a system performing cryptographic operations. These leaks can be based on **timing**, **power consumption**, or **electromagnetic emissions**. Timing attacks, a common form of side channel attack, analyze how long it takes for cryptographic algorithms to complete operations to infer sensitive information, like private keys.

### RSA Encryption
RSA is an **asymmetric encryption algorithm** that uses two keys: 
- **Public Key**: Used for encrypting messages.
- **Private Key**: Used for decrypting messages.

This project generates an RSA key pair, encrypts a message with the public key, and decrypts it with the private key. By default, RSA ensures secure communication because decryption time is constant, preventing timing-based attacks.

### Timing Attack on RSA
A **timing attack** specifically focuses on analyzing the time taken by cryptographic operations to complete. In RSA, small variations in decryption time—often due to specific private key bit patterns—could reveal details about the private key. To avoid this, secure implementations aim to keep decryption times constant, regardless of the private key's bit pattern.

### Flawed Decryption Function
To simulate a timing vulnerability, we introduce an artificial timing delay in the decryption function:
- If the least significant bit (LSB) of the private key is 1, a small delay is added to simulate a vulnerable implementation.
- This variation in decryption time could, in theory, allow attackers to deduce bits of the private key by observing decryption times, demonstrating an insecure implementation.

## Project Structure

- **generate_large_prime**: Generates large prime numbers for the RSA algorithm.
- **generate_rsa_keys**: Generates an RSA key pair.
- **encrypt**: Encrypts a message with the public key.
- **flawed_decrypt**: Simulates a decryption function with a timing vulnerability.
- **measure_flawed_decryption_time**: Measures the time taken to decrypt a message with the flawed decryption function.
- **main**: Runs the RSA key generation, encryption, flawed decryption, timing measurements, and plots the decryption times.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/Rikhil777/RSA-Timing-Attack-Simulation.git
    cd RSA-Timing-Attack-Simulation
    ```

2. Install required packages:
    ```bash
    pip install sympy matplotlib
    ```

## Running the Project
To run the project, use the following command:
```bash
python rsa.py
