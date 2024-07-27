export default function createInt8TypeArray(length, position, value) {
  const int8 = new Int8Array(length);
  if (position > int8.length) {
    throw new Error('Position outside range');
  }
  int8[position] = value;
  return int8;
}
