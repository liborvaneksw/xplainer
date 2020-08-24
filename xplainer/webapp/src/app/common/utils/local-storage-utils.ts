/**
 * Returns the current string value associated with the given in localStorage
 * or the default_value if the key does not exists.
 */
export function getLocalStorageString(key: string, default_value: string): string {
  const value = localStorage.getItem(key);
  if (!value) {
    return default_value;
  }

  return value;
}

/**
 * Returns the current integer value associated with the given in localStorage
 * or the default_value if the key does not exists.
 */
export function getLocalStorageInteger(key: string, default_value: number): number {
  const value = localStorage.getItem(key);
  if (!value) {
    return default_value;
  }

  const intValue = parseInt(value);
  if (Number.isNaN(intValue)) {
    return default_value;
  }

  return intValue;
}

/**
 * Returns the current float value associated with the given in localStorage
 * or the default_value if the key does not exists.
 */
export function getLocalStorageFloat(key: string, default_value: number): number {
  const value = localStorage.getItem(key);
  if (!value) {
    return default_value;
  }

  const floatValue = parseFloat(value);
  if (Number.isNaN(floatValue)) {
    return default_value;
  }

  return floatValue;
}

/**
 * Returns the current float value associated with the given in localStorage
 * or the default_value if the key does not exists.
 */
export function getLocalStorageBoolean(key: string, default_value: boolean): boolean {
  const value = localStorage.getItem(key);
  if (!value) {
    return default_value;
  }
  return value && value.toLocaleLowerCase() === "true";
}
