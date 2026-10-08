**Proposal: Eclipse Temurin OpenJDK 25 (LTS)**

I propose using **Eclipse Temurin 25** as our OpenJDK distribution for both Windows development and the Linux container runtime.

**1. Why Eclipse Temurin?**

- Eclipse Temurin is an OpenJDK distribution maintained by Eclipse Adoptium (Eclipse Foundation).
- It provides Java SE-compatible, tested OpenJDK binaries.
- Unlike Oracle's OpenJDK builds from `jdk.java.net`, Temurin continues providing security updates for LTS versions.

**2. License**

- License: **GPLv2 with Classpath Exception**.
- Free for commercial use, including production environments.
- No Oracle Java SE subscription or paid support contract is required.
- Standard open-source license obligations still apply.

**3. LTS**

Java 25 is designated as an **LTS release** by Eclipse Adoptium.

Temurin 25 updates are planned until **at least September 2031**, with community maintenance.

Therefore, we can retain our original decision to migrate to JDK 25 for long-term maintainability.

**4. Downloads (25.0.4.1+1)**

Windows x64 (ZIP):

https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25.0.4.1%2B1/OpenJDK25U-jdk_x64_windows_hotspot_25.0.4.1_1.zip

Linux x64 (TAR.GZ):

https://github.com/adoptium/temurin25-binaries/releases/download/jdk-25.0.4.1%2B1/OpenJDK25U-jdk_x64_linux_hotspot_25.0.4.1_1.tar.gz

**Official references**

- License FAQ: https://adoptium.net/docs/faq
- LTS support roadmap: https://adoptium.net/support/
- Official release: https://github.com/adoptium/temurin25-binaries/releases/tag/jdk-25.0.4.1%2B1

Please confirm whether Eclipse Temurin is acceptable under the customer's OSS policy so that we can proceed with the download request.
