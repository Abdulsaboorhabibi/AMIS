/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../../AMIS/**/*.{html,js}",
  './node_modules/flowbite/**/*.js',
  ],
  theme: {
    extend: {
      screens: {
        print:{ raw : 'print' }
      }
    },
  },
  plugins: [
    // use form plugins
    require("@tailwindcss/forms"),
    require('flowbite/plugin'),
  ],
};
