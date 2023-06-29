// const checkId = document.getElementById('checkIdShowCard');

// const checkBtn = document.getElementById("checkIdShowCardBtn");

// const submitCheckBtn = document.querySelector('#submitCheckBtn');

// checkBtn.addEventListener('click', ()=>{
//     checkId.classList.add('showCheckCard');
// });


// function getCookie(name){
//     let cookieValue = null;
//     if(document.cookie && document.cookie !== ''){
//         const cookies = document.cookie.split(';');
//         for(let i = 0; i< cookies.length; i++){
//             const cookie = cookies[i].trim();

//             if (cookie.substring(0, name.length + 1) === (name + '=')){
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }

//     return cookieValue;
// }

// const csrftoken = getCookie('csrftoken');

// submitCheckBtn.addEventListener('click', (e)=>{
//     e.preventDefault()
//     const urls = 'http://127.0.0.1:8000/visitors/check_visitor/'
//     fetch(urls,  {
//         method: 'POST',
//         credentials: 'same-origin',
//         headers: {
//             'Accept': 'application/json',
//             'X-Requested-With': 'XMLHttpRequest',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({
//             id_number : document.querySelector('#idInput').value
//         })
//     })
//     .then(response => {
//         result = response.json()
//         status_code = response.status;
//         if (status_code != 200){
//             console.log(status_code)
//             return false;
//         }
//         return result
//     })
//     .then(result => {
//         console.log(result)
//     })

//     .catch(error=> {
//         console.log(error)
//     })
// });


// const registerVisitorBtn = document.querySelector('#registerVisitorBtn');
// const registerIdShowCard = document.querySelector('#registerIdShowCard');
// const register = () => {
//     registerIdShowCard.classList.remove('hideRegisterCard');
//     registerIdShowCard.classList.add('showRegisterCard');
// }

// registerVisitorBtn.addEventListener('click', register);


// const submitRegisterBtn = document.querySelector("#submitRegisterBtn");


// submitRegisterBtn.addEventListener("click",  (e) => {
//     e.preventDefault()
//     const reg_urls = 'http://127.0.0.1:8000/visitors/visitor_register/'
//     fetch(reg_urls,  {
//         method: 'POST',
//         credentials: 'same-origin',
//         headers: {
//             'Accept': 'application/json',
//             'X-Requested-With': 'XMLHttpRequest',
//             'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({
//             firstName : document.querySelector('#firstName').value,
//             middleName : document.querySelector('#middleName').value,
//             lastName : document.querySelector('#lastName').value,
//             gender : document.querySelector('#gender').value,
//         }),
      
        
//     })
    
//     .then(response => {
//         result = response.json()
//         status_code = response.status;
//         if (status_code != 200){
//             console.log(status_code)
//             return false;
//         }
//         return result
//     })
//     .then(result => {
//         console.log(result)
//     })

//     .catch(error=> {
//         console.log(error)
//     });

// });

