export default function createInt8TypeArray(length, position, value) {
  const int8 = new Array(length);
  int8[position] = value;
  return int8;
}
