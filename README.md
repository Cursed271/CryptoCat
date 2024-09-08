# CryptoCat

## Project Description

CryptoCat is a Python script designed to assess the effectiveness of Endpoint Detection and Response (EDR) solutions implemented within an organization. As a ransomware simulator, CryptoCat empowers penetration testers by simulating ransomware attacks to evaluate how well an organization’s EDR system can detect and respond to such threats.

> With CryptoCat, conducting realistic ransomware simulations becomes a streamlined process for penetration testers. The script simulates various ransomware behaviors, allowing security professionals to test the response capabilities of their EDR solutions. By simulating these attacks, CryptoCat provides valuable insights into how well an organization’s defenses hold up against real-world ransomware scenarios, helping identify gaps and improve overall security posture.

> Whether you are an experienced security expert or a burgeoning professional in the field, CryptoCat offers a practical and effective tool to enhance your security assessments. It enables you to verify and refine your EDR solution’s ability to handle ransomware threats, ensuring that your defense mechanisms are robust and resilient against potential attacks.

## Features

- Simulate Ransomware Behavior: Mimic various ransomware attack patterns to assess how well the organization’s EDR solution detects and responds to simulated threats.
- Automated Attack Scenarios: Run automated simulations of ransomware behaviors, including file encryption

## Installation

### Pre-requisites

1. Python: The script requires Python to execute. Ensure you have Python 3.6 or higher installed. You can download it from the [official Python website](https://www.python.org/downloads/).
2. Python Libraries: CryptoCat depends on several Python Libraries. These will be installed automatically when you run the `pip install -r requirements.txt`. 
3. Authorization: Ensure you have explicit authorization to simulate ransomware attacks and encrypt files on the organization's systems to comply with legal and ethical guidelines.

### Installation Steps

1. Clone the project using "git clone"
2. Go to the project directory: ```cd CryptoCat```
3. Install dependencies: ```pip3 install -r requirements.txt```
4. Run CryptoCat: ```python3 CryptoCat.py```

## Usage

To use **CryptoCat**, follow these steps:

1. Specify Folder: Enter the path in the script to the folder containing the files that you wish to encrypt or decrypt. The script will process all files within this directory.
2. Run the script: ```python3 CryptoCat.py```

## Screenshots

![CryptoCat](https://github.com/Cursed271/CryptoCat/blob/main/CryptoCat.png)

## Script Configuration

Before running the script, you need to enter the path of the folder that you want to encrypt. 
1. Open the CryptoCat.py script in a Text Editor.
2. Locate the Global Declaration section.
3. Replace the placeholder values with the path of the folder you want to encrypt. 

## Contribution

1. Create a personal copy of the project by forking the repository on Github
2. Make a new branch for your changes
3. Implement your improvements or fixes
4. Commit your changes and push them to your fork
5. Submit a pull request from your branch to the main repository
6. Respond to any feedback and make revisions as needed

## License

This project is licensed under the GPLv3 License. See the LICENSE file for details. 

### Summary

- Freedom to Use: You can use, modify, and distribute the software for any purpose. 
- Source Code Access: The source code is available, and you can modify it to suit your needs. 
- Copyleft: Any derivative work must also be distributed under the same GPL license, ensuring that all modifications remain open and free
- No Warranty: The software is provided "as-is" without any warranty of any kind. The author is not liable for any damages arising from the use of the software. 

## About Me

Hello, this is Steven Pereira, but most in cybersecurity refer to me as Cursed. I am from India and very much love doing Red Teaming. Presently, I work at Protiviti India Member Firm as a Senior Cybersecurity Consultant. Day to day, I do several cybersecurity-related tasks; examples include Network Reviews, web application security testing, Penetration Testing, and red teaming. I provide the implementation of security controls, audits of cloud security, and integrated information security audits.

Outside of work, I enjoy writing and contributing to various cybersecurity blogs. With my proficiency in Python development, I develop offensive cybersecurity scripts that are an integral piece for any penetration tester or red teamer. I am working on a cybersecurity book that will help and mentor junior penetration testers through some of the obstacles they might have in their early years.

When not trying to encourage cybersecurity, he can be found playing badminton, strumming his ukulele, or spending quality time with his cat and rabbits. Feel free to connect with me here on GitHub about what I am working on, and please reach out if you have any questions or would like to talk about anything in general!

- **GitHub:** [@Cursed271](https://github.com/Cursed271)
- **LinkedIn:** [@Cursed271](https://www.linkedin.com/in/cursed271/)
- **Website:** [Black Screen Of Death](https://github.com/Cursed271)

## FAQ

**Q**: Is there a way to test CryptoCat without actually encrypting files?

**A**: No, CryptoCat is designed to simulate real ransomware attacks, which involves actual encryption of files. For testing purposes, consider using a controlled environment or test system where data loss will not have significant consequences.

**Q**: How can I specify the folder for encryption or decryption?

**A**: Open the CryptoCat.py script and locate the Global Declaration section. Enter the path to the folder containing the files you wish to encrypt or decrypt. The script will process all files within this directory.

**Q**: How can I contribute to CryptoCat?

**A**: If you'd like to contribute, you can fork the repository, make your changes, and submit a pull request. Please ensure your contributions follow the project's coding standards and include relevant tests. 

**Q**: Who do I connect for support or questions?

**A**: For support or questions, you can open an issue on the Github repository or contact me directly through the provided communication channels in this README file. 