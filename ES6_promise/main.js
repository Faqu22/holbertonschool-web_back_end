import handleResponseFromAPI from './2-then';

const promise = Promise.resolve();
const a = handleResponseFromAPI(promise);
console.log(a);
