# MyRestaurant
![Presentation video](media/restaurant_logos/restaurant-menu.mp4)
[![Video](media/restaurant_logos/Screenshot%20from%202024-06-11%2019-11-40.png)](media/restaurant_logos/restaurant-menu.mp4)
<iframe width="560" height="315" src="media/restaurant_logos/restaurant-menu.mp4" frameborder="0" allowfullscreen></iframe>

## Introduction

MyRestaurant is a dynamic and efficient restaurant menu manager. It allows reataurant owners to easily keep their menus up to date without having to print new ones every time there is an update, and the customer will just have to scan the QRCode of the restaurant and see their menu. For a live demo, visit [https://ludivsolutions.tech/]. To learn more about the development process and features, check out the [Final Project Blog Article].

- **Deployed Site**: [https://ludivsolutions.tech/](https://ludivsolutions.tech/)
- **Final Project Blog Article**: [Final Project Blog Article URL]
- **Author(s)**:
  - Ludivin Senunda tchouapi - [https://www.linkedin.com/in/ludivin-seunda-1593641ba/](https://www.linkedin.com/in/ludivin-seunda-1593641ba/)
  - Aisha Hammed - [Author 2 LinkedIn URL]

## Installation

To run MyRestaurant locally, follow these steps:

1. Clone the repository:

```bash
git clone [https://github.com/RHEZUS/MyRestaurant.git](https://github.com/RHEZUS/MyRestaurant.git)
cd MyRestaurant
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up the database:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Access the application at `http://localhost:8000/` in your web browser.

## Usage

- MyRestaurant can be used for:
Restaurant Management: Users can use the application to manage various aspects of restaurants, including adding, updating, and deleting restaurant profiles. This includes details such as restaurant name, location, contact information, and operating hours.

- Menu Management: The application allows users to create and manage menus for restaurants. This includes creating menu categories, adding items to categories, and setting availability and pricing for menu items. Users can also update menus dynamically to reflect changes in offerings or pricing.

- User Authentication and Authorization: Users can sign up for accounts, log in securely, and access features based on their roles. For example, restaurant owners may have access to administrative features like managing menus and restaurant details, while regular users may have limited access for browsing menus and making orders.

- QR Code Generation: The application generates QR codes for restaurants, possibly linking to their menus or other relevant information. This feature can facilitate contactless menu browsing for customers by allowing them to scan QR codes with their smartphones to access the restaurant's menu directly.

## Contributing

We welcome contributions from the community! To contribute to [Project Name], follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## Related Projects

Here are some related projects:

- [getscanmenu.com](https://getscanmenu.com/)
- [TouchBistro](https://www.touchbistro.com/features/ipad-menu-management/)

## Images
![Presentation video](media/restaurant_logos/Screenshot%20from%202024-06-05%2022-01-11.png)
![Presentation video](media/restaurant_logos/Screenshot%20from%202024-06-11%2019-12-07.png)
![Presentation video](media/restaurant_logos/Screenshot%20from%202024-06-11%2019-11-40.png)