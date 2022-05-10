module.exports = {
    content: ["./*.{html,js}"],
    theme: {
        extend: {
            screens: {
                'short': { 'raw': '(max-height: 700px)' },
                // => @media (max-height: 700px) { ... }
                'tiny': { 'raw': '(max-width: 300px)' },
            }
        },
        fontFamily: {
            'open-sans': ['"Open Sans"', 'sans-serif'],
            'comfortaa': ['Comfortaa', 'cursive'],
            'roboto': ['Roboto', 'sans-serif'],
            'roboto-flex': ['"Roboto Flex"', 'sans-serif'],
            'helvetica': ['Helvetica', 'sans-serif']
        }
    },
    plugins: [
        require('tailwindcss'),
        require('autoprefixer'),
    ],
}