// const emailInput = document.getElementById('registration_email');
// const pattern = /[a-zA-Z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,3}$/;

// if (pattern.test(emailInput.value)) {
//   // The input field contains an @ symbol and a . symbol
//   emailInput.style.backgroundColor = '#00FF00';
// } else {
//   emailInput.style.backgroundColor = '';
// }


const emailInput = document.getElementById('email');
const resultDiv = document.getElementById('result');

emailInput.addEventListener('change', () => {
  const email = emailInput.value;

  // send an AJAX request to the server to check the email
  const xhr = new XMLHttpRequest();
  xhr.open('GET', `/check_email/${email}`);
  xhr.onload = () => {
    if (xhr.status === 200) {
      resultDiv.innerHTML = xhr.responseText;
    }
  };
  xhr.send();
});