# Avishay Tal - Academic Website

A modern, responsive academic website built with Jekyll and GitHub Pages, featuring a clean design optimized for academic content.

## 🌟 Features

- **Modern Design**: Clean, professional layout with academic-focused styling
- **Responsive**: Fully responsive design that works on desktop, tablet, and mobile
- **Fast Loading**: Optimized for performance with minimal dependencies
- **SEO Optimized**: Proper meta tags and structured content
- **Accessible**: Built with accessibility best practices
- **GitHub Pages Ready**: Configured for easy deployment on GitHub Pages

## 🚀 Quick Start

### Prerequisites

- Ruby 2.7 or higher
- Bundler gem
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Serve locally**
   ```bash
   bundle exec jekyll serve
   ```

4. **View the site**
   Open [http://localhost:4000](http://localhost:4000) in your browser

### Deployment to GitHub Pages

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Enable GitHub Pages**
   - Go to your repository settings
   - Navigate to "Pages" section
   - Select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Save the settings

3. **Access your site**
   Your site will be available at `https://yourusername.github.io/your-repo-name`

## 📁 Project Structure

```
├── _config.yml          # Jekyll configuration
├── _layouts/            # Page layouts
│   ├── default.html     # Default layout
│   └── home.html        # Homepage layout
├── assets/              # Static assets
│   ├── css/
│   │   └── main.css     # Main stylesheet
│   └── js/
│       └── main.js      # JavaScript functionality
├── index.md             # Homepage content
├── Gemfile              # Ruby dependencies
├── preview.html         # Static preview file
└── README.md            # This file
```

## 🎨 Customization

### Colors and Typography

The website uses CSS custom properties for easy theming. Edit `assets/css/main.css` to customize:

```css
:root {
    --primary-color: #1a365d;    /* Main brand color */
    --secondary-color: #2d3748;  /* Secondary text color */
    --accent-color: #3182ce;     /* Accent color for links */
    --text-color: #2d3748;       /* Main text color */
    --bg-color: #ffffff;         /* Background color */
    --bg-light: #f7fafc;         /* Light background */
    --border-color: #e2e8f0;     /* Border color */
}
```

### Content Updates

- **Homepage**: Edit `index.md` to update your main content
- **Navigation**: Modify `_layouts/default.html` to update the navigation menu
- **Styling**: Update `assets/css/main.css` for design changes

### Adding New Pages

1. Create a new `.md` file in the root directory
2. Add front matter at the top:
   ```yaml
   ---
   layout: default
   title: "Your Page Title"
   ---
   ```
3. Add your content below the front matter

## 📱 Responsive Design

The website is fully responsive with breakpoints at:
- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px

## 🔧 Technical Details

### Built With

- **Jekyll**: Static site generator
- **GitHub Pages**: Hosting platform
- **CSS Grid & Flexbox**: Modern layout techniques
- **CSS Custom Properties**: For theming
- **Inter Font**: Modern typography
- **JetBrains Mono**: Code font

### Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📄 Content Sections

The website includes the following main sections:

- **Research Interests**: Your main research areas
- **Publications**: Academic publications with proper formatting
- **Teaching**: Course history and information
- **Contact Information**: Office location and email
- **Group Information**: Current and former students
- **Program Committees**: Conference service
- **Events**: Workshops and programs

## 🎯 SEO Features

- Semantic HTML structure
- Meta tags for social sharing
- Open Graph tags
- Twitter Card support
- Structured data markup
- Fast loading times
- Mobile-friendly design

## 📊 Performance

- Optimized CSS and JavaScript
- Minimal dependencies
- Fast loading times
- Efficient image handling
- Clean, semantic HTML

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you have any questions or need help with the website, please:

1. Check the [Issues](https://github.com/yourusername/your-repo-name/issues) page
2. Create a new issue if your question isn't already answered
3. Contact: atal@berkeley.edu

## 🙏 Acknowledgments

- Built with [Jekyll](https://jekyllrb.com/)
- Hosted on [GitHub Pages](https://pages.github.com/)
- Fonts from [Google Fonts](https://fonts.google.com/)
- Icons from [Feather Icons](https://feathericons.com/)
