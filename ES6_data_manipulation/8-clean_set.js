export default function cleanSet(set, string) {
  if (typeof string !== 'string' || string === '') {
    return '';
  }
  const reault = [];
  for (const value of set) {
    if (value.startsWith(string)) {
      result.push(value.slice(string.length));
	}
  }

  return result.join('-');
}
