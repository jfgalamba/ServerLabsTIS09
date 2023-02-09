import { 
    installValidators,
    validateAllFields,
    resetAllFields,
    addPredicates,
} from './validations.js';

import {
    bySel,
    whenClick,
    syncWait,
    isValidDate,
    byPOSTasJSON,
} from './utils.js';


const URL = 'http://127.0.0.1:8000';
const tournamentID = 1;

addPredicates({
    fullName           : /^\p{Letter}{2,}( \p{Letter}{2,})+$/u,
    password           : { 
        expr: /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[#$%&]).{6,10}$/,
        showSuccess: true,
    },
    confirmPassword     : {
        expr: confirmPassword,
        showSuccess: true,
    },
    'date_DD/MM/YYYY'  : isValidDate,
    phoneNumber        : /^(\+\d{3})?\d{9}$/,
});

window.addEventListener('load', function() {
    installValidators();
    whenClick('reset', e => resetAllFields());
    whenClick('submit', validateAndSubmitForm);
});

/**
 * @param {Object} responseData 
 */
function showSuccess(responseData) {
    const msg = `Inscrição realizada com sucesso.<br>
Player: ${responseData.full_name} <br>
ID: ${responseData.id} <br>
Email: ${responseData.email}`;
    const formFields = document.querySelector('.info');
    formFields.style.display = 'none';
    const elemsToHide = document.querySelectorAll('form > button, .checkbox');
    elemsToHide.forEach(elem => elem.style.display = 'none');
    showSubmissionInfo(msg, true);
}

/**
 * @param {Object} responseData 
 */
function showError(responseData) {
    const msg = `Não foi possível concluir a inscrição. ${responseData.detail}`;
    showSubmissionInfo(msg, false);
}

function showSubmissionInfo(msg, success) {
    const submissionStatusElem = document.querySelector('.submission-status');
    const [cssClassToAdd, cssClassToRem] = (success ? 
          ['submission-status-ok', 'submission-status-error'] 
        : ['submission-status-error', 'submission-status-ok'] 
    );
    submissionStatusElem.innerHTML = `${msg}`;
    submissionStatusElem.classList.add(cssClassToAdd);
    submissionStatusElem.classList.remove(cssClassToRem);
}

function confirmPassword(passwd2) {
    const passwd1 = document.getElementById('password').value;
    return passwd1 && passwd1 === passwd2;
}

