import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise
    .allSettled([signUpUser(firstName, lastName), uploadPhoto(filename)])
    .then((response) => (
      response.map((i) => ({
        status: i.status,
        value: i.status === 'fulfilled' ? i.value : String(i.reason),
      }))
    ));
}
