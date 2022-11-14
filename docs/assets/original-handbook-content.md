# Welcome to BGS Informatics onboarding

<!-- TOC -->

- [Welcome to BGS Informatics onboarding](#welcome-to-bgs-informatics-onboarding)
- [Introduction](#introduction)
- [Handbook aims](#handbook-aims)
- [Continuous improvement](#continuous-improvement)
- [Key contacts](#key-contacts)
- [Key Resources](#key-resources)
- [Helpful tools](#helpful-tools)
  - [Communication](#communication)
  - [Security](#security)
  - [Being on-site](#being-on-site)
  - [Remote working](#remote-working)
- [First ten days](#first-ten-days)
- [Network](#network)
  - [OneDrive](#onedrive)
- [How do we work?](#how-do-we-work)
- [Technologies and other resources](#technologies-and-other-resources)
  - [Career Development](#career-development)
    - [Training resources](#training-resources)
      - [Online Training](#online-training)
      - [BGS training](#bgs-training)
        - [Highlighted BGS training courses](#highlighted-bgs-training-courses)
    - [Attendance of conferences & events](#attendance-of-conferences--events)
  - [Specific onboarding topics](#specific-onboarding-topics)
  - [Java](#java)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
  - [JavaScript](#javascript)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
    - [Websites](#websites)
    - [Specific training](#specific-training)
  - [Git](#git)
      - [Tooling](#tooling)
      - [Suggestions for documentation](#suggestions-for-documentation)
  - [Development Environment](#development-environment)
    - [Setting up WSL2 with VSCode post CE+](#setting-up-wsl2-with-vscode-post-ce)
    - [Setting up Cypress for Angular application post CE+](#setting-up-cypress-for-angular-application-post-ce)
      - [Available documentation](#available-documentation)
  - [Python](#python)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
  - [User Experience](#user-experience)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Documentation](#documentation)
    - [Tooling](#tooling)
  - [UI Design](#ui-design)
    - [Useful articles](#useful-articles)
  - [Databases](#databases)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Naming Conventions](#naming-conventions)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
      - [Flyway](#flyway)
        - [SQL script naming conventions:](#sql-script-naming-conventions)
  - [DevOps](#devops)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
  - [National Geoscience Data Centre NGDC](#national-geoscience-data-centre-ngdc)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
  - [Corporate data management](#corporate-data-management)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
  - [NGDC Grant management](#ngdc-grant-management)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
  - [Digital preservation](#digital-preservation)
    - [MS Teams channels](#ms-teams-channels)
    - [Key contacts](#key-contacts)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
    - [Tooling](#tooling)
- [FAQ](#faq)
- [Informatics teams](#informatics-teams)
  - [Team Geosemantics](#team-geosemantics)
    - [Contacts](#contacts)
      - [Available documentation](#available-documentation)
      - [Suggestions for documentation](#suggestions-for-documentation)
  - [Team GeoSpatial](#team-geospatial)
    - [Available documentation](#available-documentation)
    - [Suggestions for documentation](#suggestions-for-documentation)
  - [Team Data Science](#team-data-science)
      - [Contacts](#contacts)
      - [Available documentation](#available-documentation)
      - [Suggestions for documentation](#suggestions-for-documentation)
  - [Team Data Delivery and Licencing](#team-data-delivery-and-licencing)
      - [Contacts](#contacts)
      - [Available documentation](#available-documentation)
      - [Suggestions for documentation](#suggestions-for-documentation)
  - [Team Statistics](#team-statistics)
      - [Contacts](#contacts)
      - [Available documentation](#available-documentation)
      - [Suggestions for documentation](#suggestions-for-documentation)
  - [Team Visualisation](#team-visualisation)
      - [Contacts](#contacts)
      - [Available documentation](#available-documentation)
      - [Suggestions for documentation](#suggestions-for-documentation)
- [Glossary](#glossary)
- [Additional reading](#additional-reading)

<!-- /TOC -->

![decoration-divider](assets/onboarding-end.svg)


# Introduction

This onboarding document aims to get new starters up to speed with BGS Digital processes, tools, sources of information and general signposting of content. The content is being formatted with markdown for time being to speed up the content creation process. A future work package will look at creating an effective GUI e.g. static site from the content.

# Handbook aims

- :x: **NOT** a replacement for HR and H&S process
- :x: **NOT** a formal signoff document that forms part of personnel files
- :x: **NOT** to duplicate content elsewhere on BGS systems
- :white_check_mark: **IS** aiming to signpost and direct to the most current source of truth
- :white_check_mark: **IS** a living document to help new starters into Digital get up to speed
- :white_check_mark: **IS** missing content but starting with a minimum viable product (MVP) and expanding

# Continuous improvement

:star: In the interests of paying it forward, we encourage you to suggest changes and updates to this issue and the handbook, both of which can be done via Merge Request (MR).

# Key contacts

- IT issues (e.g. software/hardware): contact Systems and Network Support (SNS). Location specific support for [Keyworth](mailto:kwhelp@bgs.ac.uk) or [Edinburgh](mailto:mnhelp@bgs.ac.uk)
- Estate issues (e.g. office, desks, chairs, car parks): [fmhelp@bgs.ac.uk](mailto:fmhelp@bgs.ac.uk)
- HR issues: [bgspers@bgs.ac.uk](mailto:bgspers@bgs.ac.uk)
- Become a BGS library member: [libuser@bgs.ac.uk](mailto:libuser@bgs.ac.uk) (Library Help Desk, Keyworth)
- [BGS Organograms](http://bgsintranet/corporate/organograms.html)
# Key Resources

- [BGS intranet](http://bgsintranet/)
  - Only available when connected to the BGS Network
- [BGS GitLab](https://kwvmxgit.ad.nerc.ac.uk/)
  - Sign in with your NERC username and password
- [BGS GitHub organisation](https://github.com/BritishGeologicalSurvey)
  - You will need a GitHub account which has been secured with 2FA. Contact @stever to be added to the BGS GitHub organisation account
- [BGS website](https://www.bgs.ac.uk/)
  - The public face of BGS, provides links to [BGS datasets](https://www.bgs.ac.uk/geological-data/datasets/) and key [map viewers](https://www.bgs.ac.uk/geological-data/map-viewers/) available to the public.

---
# Helpful tools

On Windows PCs, the Company Portal is the primary way to install software that has been corporately approved. It is pre-installed and available from the start menu.

<details>
<summary>View Company Portal screenshot</summary>
<br>

![company portal screenshot](assets/screenshots/company-portal.png)
</details>

## Communication

- [Zoom](https://zoom.us/)
  - Sign in using `SSO` then enter `UKRI`.
  - You may be asked to sign in again using Microsoft single sign-on
- [Microsoft Teams](https://www.microsoft.com/en-gb/microsoft-teams/log-in)
  - Search for/ask for invite to `BGS Digital Data Products and Applications`
- Microsoft Outlook
  - [BGS template signature](\\kswan\Publications\Documents\BGS Templates\Outlook signature)
  - Desktop clients
    - Install [Zoom for Outlook](https://support.zoom.us/hc/en-us/articles/200881399-Microsoft-Outlook-Plugin-Desktop-) to integrate Zoom meetings into calendar appointments.
  - Web client: https://webmail.nerc.ac.uk/
- [Miro](https://miro.com)
  - Virtual whiteboard tool used for collaboration when working remotely. Ask to be invited into the `BGS_DigitalPlanning` group (currently free plan limited to 3 editable boards). If you need a persistent board contact @cats or @pautva who will create a password-protected board for you.
- [Loom](https://www.loom.com/)
  - Record up to 5 minutes of your screen (with optional talking head) to share content, run a demonstration or record a how-to guide without having to write everything down.


## Security
- Microsoft Authenticator app ([iOS](https://apps.apple.com/gb/app/microsoft-authenticator/id983156458) and [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator&gl=US) app)
  - Used to authenticate sign in to BGS web systems using your standard login credentials. Needs to be set up in coordination with [SNS](#key-contacts).
    - Download the app to your mobile device
    - Click + to `Add account` > `Work or school account` and sign in with your NERC login credentials.
- [Nexus Sonatype Repository Manager](https://nexus-internal.bgs.ac.uk/)
  - If you use any dependency tools like `npm`, `maven` or `PyPI` then you will need to configure your tooling to use the BGS internal Nexus repo. Contact @jostev or @decval for more information.

## Being on-site
- [Setting up printers in your office](http://bgsintranet/IT-security-application-development/IT-services/printing.html)
- Connecting to WiFi networks on-site
  - [GovWifi](https://www.wifi.service.gov.uk/connect-to-govwifi/) - cross-site network
  - BGS Guest network - connect to the WiFi and register for a username/password to login again
  - BGS Developer - a network for testing applications using development devices. If needed you will need to contact [SNS](#key-contacts) and provide your development device MAC address.

## Remote working
- Connect to the BGS network to use applications locally
  - https://pulse.bgs.ac.uk/mfa
- Connect to a Remote Desktop machine on the network
  - https://portal.bgs.ac.uk/mfa

# First ten days

| Day         | Area of Focus                                                                                                                                                                                                                                                                                                  |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Day 01**  | HR induction and H&S induction (may be later in week), user accounts (NERC, Oracle/UKSBS), office wifi, MFA setup, site tour, meeting team members, introduction to key systems (UKSBS, GitLab), exploration of existing projects/repos, (if dev) request local admin which is needed to install some software |
| **Day 02**  | Install tooling for role, setup tooling (e.g. IDE setup) get account for OReily learning, identify projects which can help onboard                                                                                                                                                                             |
| **Day 03**  | Role-specific training and introduction to existing projects                                                                                                                                                                                                                                                   |
| **Day 04**  | Role-specific training and introduction to existing projects                                                                                                                                                                                                                                                   |
| **Day 05**  | Explore (Various)                                                                                                                                                                                                                                                                                              |
| **Day 06+** | Explore (Various)                                                                                                                                                                                                                                                                                              |


# Network

The default [network drive mappings](http://bgsintranet/data/project-data/san-drives.html) should be available when you first login to your machine. If not please contact [SNS](#key-contacts).

- `P:` - Public folder for sharing across BGS internal network. This folder is wiped on a weekly basis.
- `N:` - Private network folder which is only accessible to your username.
- `S:` - BGS corporate data
- `W:` - BGS project data

[Oracle](https://www.oracle.com/uk/database/) is the primary data store for BGS corporate data. @mln is the Database Architect and primary contact for DB queries.
## OneDrive

Sign in with NERC credentials to access storage. Useful when working on and off the Pulse network.
# How do we work?

Our product development process usually follows Agile methodology. You can learn more about Agile principles here:
* [Video - Agile Product Ownership in a Nutshell](https://www.youtube.com/watch?v=502ILHjX9EE)
* [Dinner Orders Training Course - Software Project Management in GitLab](https://kwvmxgit.ad.nerc.ac.uk/jostev/dinner-orders)

For projects that require more clarity, we might run a design sprint or conduct other research activities. You can learn more about them here:
* [What is a design sprint?](http://digital-planning.glpages.ad.nerc.ac.uk/design-toolkit/docs/1-intro-what-is-it/)
* [User research methods](http://digital-planning.glpages.ad.nerc.ac.uk/design-toolkit/docs/10-method-1-understand/)

# Technologies and other resources

These contact details are non-exhaustive but provide a starter contact.

## Career Development

The Learning & Development team are awaiting a report from the appraisal system showing what L&D staff have requested. It is well worth staff (especially new staff) discussing any training requests with their line manager and adding them onto their forward job plan/appraisal as they will be picked up. L&D will use this information to help them determine how they spend their budgets.

### Training resources
#### Online Training
- [O'Reilly Training](https://www.oreilly.com/member/login/) - Contact [SNS helpdesk](mailto:kwhelp@bgs.ac.uk) if you need to request an account
- [Learning Tree](https://www.learningtree.com/) - BGS has access to subsidised training courses if required
- [ESRI UK Training](https://store.esriuk.com/learning/catalogue/#-)
- [Pluralsight](https://www.pluralsight.com/) - Used by several staff so far but hits a paywall after 10 hours.
- [Learn to use GitLab](https://kwvmxgit.ad.nerc.ac.uk/jostev/dinner-orders) - John Stevenson's (@jostev) Diner Orders Training Course
- [Version control with Git](http://training.glpages.ad.nerc.ac.uk/git-novice/_site/) - Software carpentry course (@mase, @jostev, @decval)

#### BGS training
 - [BGS Learning & Development](http://bgsintranet/corporate/learning-development.html)

##### Highlighted BGS training courses
- Introduction to Geology - The course is aimed at BGS staff who have had no or minimal geological training and runs as a series of weekly 2 hour  sessions followed by a one day field trip. This course is very popular and will run when enough staff are signed up to it.
### Attendance of conferences & events
- Apply for funding via the [Conference committee funding](http://bgsintranet/corporate/human-resources/career-appraisal/career-development/conference-committee-funding.html)

## Specific onboarding topics

- [BGS GitLab onboarding](onboarding-gitlab.md)

## Java

<details>
<summary>View Java resources</summary>
<br>

---
### MS Teams channel(s)
- [Discuss Java (and JVM languages)](https://teams.microsoft.com/l/channel/19%3a052362450ff443dfa13753418a627f80%40thread.skype/Discuss%2520Java%2520(and%2520JVM%2520languages)?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [Marcus Sen](@mase)
- [Rachel Heaven](@reh)

### Available documentation

### Suggestions for documentation

### Tooling

---
</details>

## JavaScript

<details>
<summary>View JavaScript resources</summary>
<br>

---
### MS Teams channel(s)
- [Discuss JavaScript](https://teams.microsoft.com/l/channel/19%3ab0beea7746dd46f98253680a0e6c4309%40thread.skype/Discuss%2520JavaScript?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [Steve Richardson](@stever)

### Available documentation
- [How to setup `npm` to use BGS Nexus for dependencies](https://kwvmxgit.ad.nerc.ac.uk/-/snippets/114)
### Suggestions for documentation

- How to setup Windows 10 machine to use `nvm-windows` [link](https://github.com/coreybutler/nvm-windows)
- Installing and setting up `bash` terminal on Windows 10
- How to setup a template `.bashrc` file in correct home directory with recommended settings e.g. `source ~/nvm/nvm.sh`
- How to add your credentials to Windows Credential manager for connecting to GitLab without entering your username/password each time.

### Tooling
- VSCode
  - Recommended  extensions:
    - [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)
    - [GitLab Workflow](https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow)
    - [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
    - [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
    - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
    - [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
    - [Version Lens](https://marketplace.visualstudio.com/items?itemName=pflannery.vscode-versionlens)

### Websites

- [Bundlephobia](https://bundlephobia.com/) Great site for visualising the impact of adding NPM dependencies

### Specific training
- [Pluralsight - Angular Fundamentals](https://www.pluralsight.com/courses/angular-fundamentals) - Used by @danwar, @dsut, @janlav
- [Codacademy Learn TypeScript](https://www.codecademy.com/learn/learn-typescript) - Used by @svea
- [Learning Typescript](https://learning.oreilly.com/library/view/learning-typescript/9781098110321/) - Pub date 2022
- [TypeScript Fundamentals challengge](https://learning.oreilly.com/scenarios/typescript-fundamentals-challenge/9781492095774/)

---

</details>









## Git

<details>
  <summary>View Git resources</summary>
  <br>

#### Tooling

  - [Git for Windows](https://git-scm.com/download/win)
  - [SourceTree](https://www.sourcetreeapp.com/)
    - Used by @janlav
  - [TortoiseGit](https://tortoisegit.org/)
  - [GitExtensions](http://gitextensions.github.io/)
    - Used by @rroth
  - Full list of GUIs listed [here](https://git-scm.com/downloads/guis)

#### Suggestions for documentation
  - Whether to use `ssh` or `https` protocol for Github/Gitlab operations, how to manage users if using SSH keys.

  Some people use [GitExtensions](http://gitextensions.github.io/) as a Graphical User Interface for itneracting with git. this can be more friendly to beginners. Talk to @rroth if you're interested in using this.

</details>

## Development Environment

<details>
  <summary>View Development Environment resources</summary>
  <br>

  ### Setting up WSL2 with VSCode post CE+
  - Follow this [Installation Guide for WSL2 on Windows 10](https://www.omgubuntu.co.uk/how-to-install-wsl2-on-windows-10) guide - You will need admin permission from SNS to use Powershell as an Administrator. DO NOT INSTALL Ubuntu 20.04 (step4) there are compatibility issues with this version, install 18.04 also avaliable from the windows store.
  - After completing the steps in the guide above, boot up VSCode and install the 'Remote WSL' extension. Select the green remote indicator in the lower left corner of the status bar, then select 'Remote-WSL: New Window using Distro...' selecting the version of Ubuntu you downloaded earlier.

  ### Setting up Cypress (for Angular application) post CE+
  - Open up your project of choice.
  - Run: `npm install cypress --save-dev`
  - Run: `sudo apt update`
  - Run: `apt-get install libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb`
  - Open up Company Portal
  - Download 'BGS - MobaXterm'
  - On the initial boot of the application you will be presented with a firewall alert, select all three options (Domain, Private, Public) and continue. You will need admin privileges from SNS to proceed.
  - Go to Settings > X11 > set X11 remote access = full
  - In the settings window go to Misc > check 'Allow multiple instances of MobaXterm'
  - In a WSL terminal go to home/<username> (if you open up the version of Ubuntu you downloaded you will be at the correct root) and execute `code .bashrc` . This will open a VSCode editor.
  - Add the following code:
  ```
  # set DISPLAY variable to the IP automatically assigned to WSL2
  export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2; exit;}'):0.0
  sudo /etc/init.d/dbus start &> /dev/null
  ```
  - Save and close the .bashrc file then run `sudo visudo -f /etc/sudoers.d/dbus`
  - In the editor that launches, add the following line with your username. `<your_username> ALL = (root) NOPASSWD: /etc/init.d/dbus`
  - Cypress should now be able to run in a project through WSL2.
  - This [guide](https://shouv.medium.com/how-to-run-cypress-on-wsl2-989b83795fb6) is useful, however it is not possible to use the version of X Server that they suggest.
  - **Any Issues** contact @danwar or @janlav
  <br>
  #### Available documentation
  - [Using Windows subsystem for Linux (WSL2)](https://gist.github.com/leodutra/a6cebe11db5414cdaedc6e75ad194a00) - Nice way of having a *usable* terminal on Windows
    - [Cypress requirements for WSL2](https://docs.cypress.io/guides/continuous-integration/introduction#Machine-requirements)
    - [Using Git on WSL2](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git)
    - Access WSL drive from Windows file explorer: In address bar, type: `\\wsl$`
    - To map WSL to a drive on your PC, e.g Z: drive.. In a CMD prompt run: `net use z: \\wsl$\Ubuntu-<version> /persistent:yes`
    - **Setting up Cypress with WSL2**
      - [Follow instructions here](https://shouv.medium.com/how-to-run-cypress-on-wsl2-989b83795fb6)
      - Try to run `npm run cypress:open`
      - If you receive error: `"Uncaught ReferenceError: App is not defined"`, check that WSL is set to version 2: `wsl --list -v`
      - If WSL is still set to version 1, open a Powershell window as admin & run: `wsl --set-version Ubuntu <version> 2` e.g. `wsl --set-version Ubuntu 18.04 2`
      - Restart terminal & run `npm run cypress:open` again. It should now work.
      - **N.B.** By default, the Linux distro, e.g. Ubuntu, will only have Electron browser installed for debugging with Cypress..
         So to add others, simply run: `sudo apt install firefox` or `sudo apt install chrome` etc.
    - **Snafus...**
      - If WSL doesn't start on Windows launch: Open Powershell as admin > `Get-Service vmcompute | Restart-Service`, then restart your WSL terminal.
      - If Git credentials aren't being stored.. add to .gitconfig in WSL root:
      ```
        [credential]
          helper = /mnt/c/Users/<user>/AppData/Local/Programs/Git/mingw64/libexec/git-core/git-credential-manager-core.exe
      ```
      Or wherever your local Git is installed (this may be in ProgramFiles instead of AppData)

</details>

## Python

<details>
<summary>View Python resources</summary>
<br>

---
### MS Teams channel(s)
- [Discuss Python](https://teams.microsoft.com/l/channel/19%3a4cab3e4fd4ab4c0e86f35e5bc75bb528%40thread.skype/Discuss%2520Python?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [John Stevenson](@jostev)
- [Declan Valters](@decval)

### Available documentation

- [Using the Nexus repository to install pip and conda packages](http://training.glpages.ad.nerc.ac.uk/developer-docs/nexus/packaging/python/pip/2021/07/20/conda-pip)

### Suggestions for documentation

### Tooling

---

</details>

## User Experience

<details>
<summary>View User Experience resources</summary>
<br>

---
### MS Teams channel(s)
- [Discuss User Experience (UX)](https://teams.microsoft.com/l/channel/19%3ae58b4494d1c9421a8ae2703ca248eefe%40thread.skype/Discuss%2520User%2520Experience%2520(UX)?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [Carl Watson](@cats)
- [Paulius Tvaranvicius](@pautva)

### Available documentation

- [BGS Informatics Planning toolkit](http://digital-planning.glpages.ad.nerc.ac.uk/design-toolkit/) - UX related resources: methods, workshop plans, templates, etc.

### Documentation
- [Learn how to make your first MIRO board](https://www.youtube.com/watch?v=7L1-0DOGHDY)
- [How to use Miro board to setup and run successful remote design/brainstorming sessions](http://digital-planning.glpages.ad.nerc.ac.uk/design-toolkit/docs/35-ux-workshops/)
- [Miro Design Sprint Template](https://miro.com/app/board/o9J_krWbO-c=/?invite_link_id=441898376922)

### Tooling

- [Figma Prototyping Tool](https://figma.com/)
- [BGS Corporate Colours](http://digital-planning.glpages.ad.nerc.ac.uk/design-toolkit/docs/31-bgs-corporate-colours/)
- [BGS Logos](http://digital-planning.glpages.ad.nerc.ac.uk/design-toolkit/docs/29-bgs-logos/)

---

</details>

## UI Design

<details>
<summary>View UI Design resources</summary>
<br>

---
### Useful articles
- ['Cheating' at UI design](https://medium.com/refactoring-ui/7-practical-tips-for-cheating-at-design-40c736799886) - Practical UI design tips for designers or developers

---

</details>

## Databases

<details>
<summary>View Databases to resources</summary>
<br>

BGS uses Oracle for most of its corporate datasets, but some newer projects (especially those where we work with non-BGS partners) have started using PostgreSQL.

---
### MS Teams channel(s)
- [Discuss Databases](https://teams.microsoft.com/l/channel/19%3a54b31536fd024ce486e4e53594cb6b4f%40thread.skype/Discuss%2520Databases?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [Martin Nayembil](@mln)
- [Roman Roth](@rroth)
- [Andy Bevan](@apbe)

### Available documentation

Technically there are documents available [on the intranet](http://bgsintranet/data/oracle.html), but the links are currently broken and the docs are very old.

### Naming Conventions

Database tables, views, and other objects are prefixed with a three-letter project abbreviation and an underscore, e.g. LIM_TABLENAME and GSR_VIEWNAME.

### Suggestions for documentation


### Tooling


#### Flyway
We're hoping to start using [Flyway](https://flywaydb.org/documentation/) more extensively, especially in new projects. Flyway is a tool to version-control databases. SQL files are prefixed with a number, and Flyway runs them in order and records which files were run in a table in the database.

##### SQL script naming conventions:

- Follow the file naming conventions from Flyway i.e. start with a captial "V", etc.
- When early in development and you routinely wipe and recreate teh database (i.e. before you have user data that must be preserved and prevents you from dropping and re-creating everything) use [semver](https://semver.org/) to start with. (0.1.X for table creation files, 0.2.X for dictionary data insert scripts, V9999.x for test data insertion scripts)
- keep test data insertion in separate folder - later on, you'll be able to use the flyway "locations" configuration to selectively apply only some scripts.
- Create one folder per db object. This way, you will later be able to keep ALTER scripts together with the object that they modify.
- Put Views and such in repeatable migrations - not necessary to keep in one folder per object, since they are repeatable and can just be edited directly
- After release and the db cannot be wiped and re-created, use YYYY.MM.DD.X for subsequent alter scripts e.g. `V2022.09.01.3__add_column_to_my_table.sql`


---

</details>

## DevOps

<details>
<summary>View DevOps resources</summary>
<br>

---
### MS Teams channel(s)
- [Discuss DevOps](https://teams.microsoft.com/l/channel/19%3aff7781665a5f46a88fddfe4ac8628fc1%40thread.skype/Discuss%2520DevOps?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [Wayne Shelley](@wael)

### Available documentation
- [Using the Nexus repository to manage docker containers](http://training.glpages.ad.nerc.ac.uk/developer-docs/nexus/packaging/docker/2021/07/20/docker)
- [Sitewide configuration of Nexus repositories](http://training.glpages.ad.nerc.ac.uk/developer-docs/nexus/packaging/2021/07/20/sitewide-config)
- [Pulling docker images without being sudoer](http://training.glpages.ad.nerc.ac.uk/developer-docs/docker/2021/10/13/docker-sudoers-group)

### Suggestions for documentation
- BGS implementation of Kubernetes (overview of deployment)
- Information about the staging environments (`internal-staging`, `internal-prod`, `dmz-staging`, `dmz-prod`)

### Tooling

---

</details>

## National Geoscience Data Centre (NGDC)

<details>
<summary>View NGDC resources</summary>
<br>

---
### MS Teams channel(s)
- [Data Centre)](https://teams.microsoft.com/l/channel/19%3a99828544accd49c68977f6145eafecb8%40thread.skype/Data%2520Centre?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [Garry Baker](mailto:grba@bgs.ac.uk)

### Available documentation
-	[National Geoscience Data Centre - British Geological Survey (bgs.ac.uk)](https://www.bgs.ac.uk/geological-data/national-geoscience-data-centre/) – Data Centre Homepage
### Suggestions for documentation

### Tooling

---
</details>




## Corporate data management

<details>
<summary>View corporate data management resources</summary>
<br>

---
### MS Teams channel(s)

### Key contacts
- [Claire Shelley](@clrl)

### Available documentation
-	[Data access](http://bgsintranet/data/access.html) – Internal access to BGS data.
-	[S:\GDI](//kwsan/workspace/store) – Internal viewer for BGS data.
-	[BGS GeoIndex](https://mapapps2.bgs.ac.uk/geoindex/home.html) - British Geological Survey (bgs.ac.uk) – External viewer for BGS data.
-	BGS project data management - Policies, procedures and guidelines for project data management.
-	[Digital Management Plan system](http://bgsintranet/scripts/dmps/home.cfc) – DMPs to be submitted at the start of projects.
-	Marine Portals ? - Mary

### Suggestions for documentation

### Tooling


---
</details>

## NGDC Grant management

<details>
<summary>View NGDC grant management resources</summary>
<br>

---
### MS Teams channel(s)

### Key contacts
- [Jaana Pinnick](mailto:jpak@bgs.ac.uk)

### Available documentation
-	[NGDC Guidelines and policies](http://bgsintranet/data/project-data/guidelines-policies.html) – Best practice for Research Data Management and deposit.
-	[NGDC - FAQs for NERC grants](https://www.bgs.ac.uk/download/ngdc-faqs-for-nerc-grants/) - British Geological Survey (bgs.ac.uk) – FAQs for NERC grants


### Suggestions for documentation

### Tooling

---
</details>

## Digital preservation

<details>
<summary>View Digital preservation resources</summary>
<br>

---
### MS Teams channel(s)
- [Discuss Digital Preservation](https://teams.microsoft.com/l/channel/19%3a2249016285684ff4838e664e7e79aa45%40thread.skype/Discuss%2520Digital%2520Preservation?groupId=986a7d3d-501a-4b2c-b8f5-5be979296946&tenantId=b311db95-32ad-438f-a101-7ba061712a4e)

### Key contacts
- [Jaana Pinnick](mailto:jpak@bgs.ac.uk)

### Available documentation
- [http://bgsintranet/docs/imp/BGSDigitalPreservationPolicyV2.pdf] – Best practice for embedding DP into data management processes.
- [A Basic Introduction to Digital Preservation Storage](https://blog.weareavp.com/a-basic-introduction-to-digital-preservation-storage.-part-1)
- [Digital Preservation Coalition - Handbook](https://www.dpconline.org/handbook)
- [Digital Preservation Coalition: Novice to Know-How](https://www.dpconline.org/digipres/train-your-staff/n2kh-online-training) – Free online training.

### Suggestions for documentation

### Tooling

---
</details>



# FAQ
- **Where do I find corporate applications available for installation?**<br>
Often the default user permissions on a desktop/laptop do not include admin permissions. If the software you need requires elevated permissions please [contact SNS helpdesk](#key-contacts)

- **I cannot install software X on my desktop as it says I do not have admin permissions?**<br>
Often the default user permissions on a desktop/laptop do not include admin permissions. If the software you need requires elevated permissions please [contact SNS helpdesk](#key-contacts)

- **How can I learn more about the subsurface data BGS uses and produces?**<br>
Feel free to contact [Mark Felgett](mailto:markf@bgs.ac.uk) - he offered to give a short presentation for new starters in which you'll be able to learn about the types of data BGS works with and other fun things about the subsurface.

- **Where can I fill my time sheet?**<br>
Log in to [https://ukri.changepointasp.com/](https://ukri.changepointasp.com/) and go to *My Tools > Time Sheet*

- **How do I book annual leave?**<br>
Log in to [UK SBS](https://ebs.ssc.rcuk.ac.uk/OA_HTML/OA.jsp?OAFunc=OAHOMEPAGE&oas=eGwOT5yTtqsmhdf9X_NUXg..) and go to *RCUK Self-Service Employee > Attendance Management*

- **How do I book a meeting room?**<br>
You can book meeting rooms using Microsoft Outlook. Guidance on how to do that can be found [here](https://support.microsoft.com/en-us/office/use-the-scheduling-assistant-and-room-finder-for-meetings-in-outlook-2e00ac07-cef1-47c8-9b99-77372434d3fa).

- **How do I gain read/write access to a certain project folder location?**<br>
 Please ask the project manager to request folder access by contacting the [SNS helpdesk](#key-contacts).
# Informatics teams

## Team Geosemantics

### Contacts

- @reh

#### Available documentation

- [Team documentation](https://kwvmxgit.ad.nerc.ac.uk/geosemantics/team-documentation)
#### Suggestions for documentation


## Team GeoSpatial

### Available documentation

- Adding new starter to the ESRI ArcGIS Online account (@apma)
- ArcGIS Infrastructure setup:  ([web-gis-infrastructure projects on GitLab](https://kwvmxgit.ad.nerc.ac.uk/web-gis-infrastructure))
- ([ArcGIS Online Guidance](https://kwvmxgit.ad.nerc.ac.uk/web-gis-infrastructure/agol-infra/-/wikis/AGOL-Guidance))
- How to create, serve, overwrite an ArcGIS Server map service ([Documentation](https://kwvmxgit.ad.nerc.ac.uk/web-gis-infrastructure/agol-infra/-/wikis/Publishing-from-ArcGIS-Pro-to-ArcGIS-Online))

### Suggestions for documentation

## Team Data Science

#### Contacts
#### Available documentation
#### Suggestions for documentation

## Team Data Delivery and Licencing
#### Contacts
#### Available documentation
#### Suggestions for documentation

## Team Statistics
#### Contacts
#### Available documentation
#### Suggestions for documentation

## Team Visualisation
#### Contacts
#### Available documentation
#### Suggestions for documentation
# Glossary

- **DMZ** - A DMZ network provides a buffer between the internet and an organization’s private network. The DMZ is isolated by a security gateway, such as a firewall, that filters traffic between the DMZ and a LAN. The default DMZ server is protected by another security gateway that filters traffic coming in from external networks.

- [Other BGS Acronyms on intranet](http://bgsintranet/scripts/acronyms/acronyms.cfc?method=letter&letter=D)

# Additional reading

- [NERC Digital Strategy](https://www.ukri.org/publications/natural-environment-research-council-nerc-digital-strategy-2021-2030/)
- [BGS Digital Strategy 2020-2025](https://www.bgs.ac.uk/download/bgs-digital-strategy-2020-2025/)
- [BGS Science Strategy 2019-2023: Gateway to the Earth](https://www.bgs.ac.uk/download/bgs-science-strategy-2019-2023-gateway-to-the-earth/)

