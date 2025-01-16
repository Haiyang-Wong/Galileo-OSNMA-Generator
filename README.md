# Galileo-OSNMA-Generator
This project  provides an example of implementing the TSF attack, including forging navigation data forgery, tags and subframes. This example is based on the subframes of the satellite with PRN 02 extracted from the test vectors (16\_AUG\_2023\_GST\_05\_00\_01.csv) provided by EUSPA.



#### Forging navigation data
We select the first subframe (WN = 1251, TOW = 277200) as an example and modify its ionospheric parameters, which are located on the $13$-th page of the subframe.
Below are the original and modified bits of the $13$-th page:

$0x054BC11429A07F9FC009C6875D2A80AAAAB21D\\
69F9A18E29635CF8EC0100$ (original)

$0x054BC11429A17F9FC009C6875D2A80AAAAB21D\\
69F9A18E29635CF8EC0100$ (modified)

#### Forging tag
The ionospheric parameter is located in the first navigation segment, which can be retrieved from the subframe (TOW = 277200) as follows:

$0x1311F898EE1868001F06E7AA04D76D1333662A42\\
49DD4A6EBB4CAE193D2A133FF06889EB3F5F823B\\
87F37F405AC4C0BFFBFFFB11F8001D4E9A0009901\\
2F0450A685FE7F000$ (552 bits)

We generate a message as follows by concatenating different fields according to MAC function:

$0x024E343AEE0144C47E263B861A0007C1B9EA813\\
5DB44CCD98A909277529BAED32B864F4A84CFFC1\\
A227ACFD7E08EE1FCDFD016B1302FFEFFFEC4\\
7E000753A680026404BC11429A17F9FC00$ (600 bits)

The key can be retrieved from the MACK field in the subframe with TOW = 277260 as follows:

$0xACA75FBC1C6E40A397CA7EE7EE908870$ (128 bits)

The MAC function indicated by the HKROOT field is HMAC-SHA-256. 
Taking the message and the key as input, the output from the MAC function is as follows.

$0x3C2585C882811FD8B740A5C04CE82C1FC8CA4F\\
722A018A5B32C031F9025F749C$ (256 bits)


This output is finally truncated to a 40-bit tag length indicated by the TS field, 40 bits, which is as follows:

$0x3C2585C882$ (40 bits)

The generated tag is the first tag in the subframe with TOW = 277230. 
Specifically, the 40-bit tag is divided into two parts, 32 bits and 8 bits. The 32-bit part is filled into the \emph{MACK} field of the first OSNMA portion, and the 8-bit part is filled into the \emph{MACK} field of the second OSNMA portion. 
The tag field in the first page of the subframe (TOW = 277230) is replaced by the 32-bit part as follows:

$0x021333662A4249DD4A6EBB4CAE1900BD2A5C8F\\
0961722AAAAA73F18B0100$ (replaced tag)

#### Forging subframe
The CRC value for the modified page data needs to be recalculated and replaced to the corresponding field. 
Therefore, the page associated with the ionospheric parameter in the first subframe (TOW = 2772300) needs CRC calculation, and the page associated with the first tag in the second subframe (TOW = 2772330) also needs CRC calculation.
Below are the data of the first page in the subframe (TOW = 2772300) after replacing tag and CRC:

$0x021333662A4249DD4A6EBB4CAE1900BD2A5C9E\\
8497BA6AAAAA6A9778C100$ (replaced CRC)



