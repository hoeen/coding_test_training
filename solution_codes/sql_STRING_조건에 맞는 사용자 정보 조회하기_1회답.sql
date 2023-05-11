# 9:35
# ID, 닉네임, 전체주소: 시, 도로명 주소, 상세 주소, 전화번호: 삽입
SELECT distinct(u.USER_ID), u.NICKNAME, 
        concat(u.CITY, ' ', u.STREET_ADDRESS1, ' ', u.STREET_ADDRESS2) as 전체주소,
        concat(substr(u.TLNO, 1, 3), '-', substr(u.TLNO, 4, 4), '-', substr(u.TLNO, 8)) as 전화번호
FROM USED_GOODS_BOARD as g
JOIN USED_GOODS_USER as u ON g.WRITER_ID = u.USER_ID
WHERE g.WRITER_ID in (
    SELECT g.WRITER_ID FROM USED_GOODS_BOARD as g
    GROUP BY g.WRITER_ID
    HAVING count(g.TITLE) >= 3
    )
ORDER BY u.USER_ID DESC