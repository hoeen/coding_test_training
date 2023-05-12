-- # 1:40 ~ 2:34 총 54분 걸림.. 
SELECT distinct(h.car_id), c.car_type,
    # 30일간의 대여 금액이 50만원 이상 200만원 미만
    round(c.daily_fee/100*(100-p.discount_rate) * 30) as FEE
FROM car_rental_company_rental_history as h
JOIN car_rental_company_car as c ON h.car_id = c.car_id
JOIN car_rental_company_discount_plan as p on p.car_type = c.car_type

WHERE p.duration_type in ('30일 이상') and 
    c.car_type in ('세단', 'SUV') and
    h.car_id not in 
        (
        SELECT car_id
        FROM car_rental_company_rental_history
            WHERE (start_date <= '2022-11-01' and end_date <= '2022-11-30' and end_date >= '2022-11-01') # 1 - end date가 사이에 있음
            OR (start_date <= '2022-11-30' and start_date >= '2022-11-01' and end_date >= '2022-11-30')# 2 - start date가 사이에 있음
            -- # 3 - start, end 모두 안에 있음
            OR (start_date <= '2022-11-30' and start_date >= '2022-11-01' and end_date <= '2022-11-30' and end_date >= '2022-11-01')
            -- # 4 - start, end 모두 바깥에 있음
            OR (start_date <= '2022-11-01' and end_date >= '2022-11-30')
            )
     
HAVING FEE >= 500000 and FEE <= 2000000    
ORDER BY FEE DESC, c.car_type ASC, h.car_id DESC