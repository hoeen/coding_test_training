# 9:13 시작
SELECT concat("/home/grep/src/",f.BOARD_ID,'/',f.FILE_ID,f.FILE_NAME,f.FILE_EXT) AS FILE_PATH 
FROM used_goods_file as f
LEFT JOIN used_goods_board as b ON b.BOARD_ID = f.BOARD_ID
WHERE b.VIEWS = (
    SELECT max(VIEWS) FROM used_goods_board
    )
ORDER BY f.FILE_ID DESC
# concat("/home/grep/src/",f.BOARD_ID,f.FILE_ID)