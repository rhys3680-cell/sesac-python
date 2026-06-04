def has_unique_digits(digits: list[int]) -> bool:
    """자릿수가 모두 서로 다른지 확인"""
    return len(digits) == len(set(digits))


def parse_positive_digits(text: str) -> list[int] | None:
    """문자열을 양의 정수의 자릿수 리스트로 파싱, 실패 시 None"""
    try:
        value = int(text)
    except ValueError:
        return None
    if value <= 0:
        return None
    return [int(d) for d in str(value)]


def prompt_until_valid(
    prompt: str = "서로 다른 자릿수들을 가진 양의 정수를 입력하세요: ",
) -> list[int]:
    """조건을 만족하는 입력이 들어올 때까지 반복해서 받아 자릿수 리스트로 반환"""
    while True:
        digits = parse_positive_digits(input(prompt))
        if digits is None:
            print("올바른 숫자가 아닙니다. 다시 입력해주세요.")
            continue
        if not has_unique_digits(digits):
            print("자릿수가 중복됩니다. 다시 입력해주세요.")
            continue
        return digits


def main():
    digits = prompt_until_valid()
    print(digits)


main()
