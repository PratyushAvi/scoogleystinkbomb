module.exports = {
    content: ["./*.{html,js}"],
    theme: {
        extend: {},
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