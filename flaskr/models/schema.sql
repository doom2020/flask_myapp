DROP TABLE IF EXISTS user_info;
DROP TABLE IF EXISTS session_info;

CREATE TABLE `user_info` (
`id`  bigint UNSIGNED NOT NULL AUTO_INCREMENT,
`username`  varchar(120) NOT NULL COMMENT '用户名',
`phone`  varchar(60) NOT NULL COMMENT '手机号',
`password`  varchar(1024) NOT NULL COMMENT '用户密码',
`c_time`  datetime NOT NULL COMMENT '创建时间',
`u_time`  datetime NOT NULL COMMENT '更新时间',
`is_delete`  tinyint NOT NULL DEFAULT 0 COMMENT '是否删除',
UNIQUE KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE `session_info` (
`id`  bigint UNSIGNED NOT NULL AUTO_INCREMENT ,
`session_id`  varchar(1024) NOT NULL COMMENT 'session id' ,
`username`  varchar(1024) NOT NULL COMMENT '用户名' ,
`c_time`  datetime NOT NULL COMMENT '创建时间',
UNIQUE KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;