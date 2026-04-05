const redHeaderTrigger = document.querySelector('#red_header');
const headerElement = document.querySelector('header');

redHeaderTrigger.addEventListener('click', () => {
  headerElement.style.color = '#FF0000';
});
