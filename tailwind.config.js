module.exports = {
    content: ["./*.{html,js}"],
    theme: {
        extend: {
            screens: {
                'short': { 'raw': '(max-height: 900px)' },
                // => @media (max-height: 700px) { ... }
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