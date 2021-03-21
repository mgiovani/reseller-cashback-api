[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<p align="center">
  <a href="https://github.com/mgiovani/reseller-cashback-api">
    <img src="images/logo.png" alt="Logo" width="400" height="300">
  </a>

  <h3 align="center">Reseller Cashback API</h3>

  <p align="center">
    A simple API with resellers, orders, and cashbacks endpoints.
    <br />
    <br />
    <a href="#usage">View Examples</a>
    ·
    <a href="https://github.com/mgiovani/reseller-cashback-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/mgiovani/reseller-cashback-api/issues">Request Feature</a>
  </p>
</p>



<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



## About The Project

<img src="images/admin.png" alt="Project screenshot">


### Built With

* [Django](https://www.djangoproject.com/)
* [Django REST framework](https://www.django-rest-framework.org/)
* [Pytest](https://docs.pytest.org/en/stable/)
* [Poetry](https://python-poetry.org/docs/)
* [Docker](https://www.docker.com/)


## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This are the preqrequisites you need to install to run this project.
* [Poetry](https://python-poetry.org/)
* [Python 3.9+](https://www.python.org/downloads/release/python-390/)

If you want to run this project with Docker, you will need:
* [Docker](https://www.docker.com/)
* [Docker-compose](https://docs.docker.com/compose/install/)


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mgiovani/reseller-cashback-api.git
   ```
2. Running locally:
    1. Install dependencies
       ```sh
       make install
       ```
    2. Edit envvars inside the .env file
       ```sh
       vim .env
       ```
    3. Load the .env file
       ```sh
       source .env
       ```

    3. Migrate database
       ```sh
       make migrate
       ```
    4. Run the code
       ```sh
       make run
       ```
3. Running with Docker:
    1. Copy env.example
       ```sh
       cp env.example .env
       ```
    2. Edit credentials inside the .env file
       ```sh
       vim .env
       ```
    3. Load the .env file
       ```sh
       source .env
       ```
    4. Run the code
       ```sh
       make run-docker-mode
       ```

## Usage

Check some examples of the project:

Reseller list endpoint:
<details>
  <summary>Click to show</summary>

  <img src="images/reseller.png" alt="Reseller image">
 
</details>

Order list endpoint:
<details>
  <summary>Click to show</summary>

  <img src="images/order.png" alt="Order image">
 
</details>


Accumulated cashback endpoint:
<details>
  <summary>Click to show</summary>

  <img src="images/accumulated-cashback.png" alt="Accumulated cashback image">
 
</details>


## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## License

Distributed under the MIT License. See `LICENSE` for more information.



## Contact

Giovani Moutinho - [Linkedin](https://www.linkedin.com/in/mgiovani/)

Project Link: [https://github.com/mgiovani/reseller-cashback-api](https://github.com/mgiovani/reseller-cashback-api)



[contributors-shield]: https://img.shields.io/github/contributors/mgiovani/reseller-cashback-api.svg?style=for-the-badge
[contributors-url]: https://github.com/mgiovani/reseller-cashback-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mgiovani/reseller-cashback-api.svg?style=for-the-badge
[forks-url]: https://github.com/mgiovani/reseller-cashback-api/network/members
[stars-shield]: https://img.shields.io/github/stars/mgiovani/reseller-cashback-api.svg?style=for-the-badge
[stars-url]: https://github.com/mgiovani/reseller-cashback-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/mgiovani/reseller-cashback-api.svg?style=for-the-badge
[issues-url]: https://github.com/mgiovani/reseller-cashback-api/issues
[license-shield]: https://img.shields.io/github/license/mgiovani/reseller-cashback-api.svg?style=for-the-badge
[license-url]: https://github.com/mgiovani/reseller-cashback-api/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/mgiovani
