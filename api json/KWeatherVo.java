package com.peisia.spring.mi.vo.kw;

import lombok.Data;

@Data
public class KWeatherVo {
    public Response response;

    @Data
    public static class Response {
        public Body body;

        @Data
        public static class Body {
            public String dataType;
            public Items items;

            @Data
            public static class Items {
                public Item item;

                @Data
                public static class Item {
                    public String stnNm;
                    public String minTa;
                    public String maxTa;
                }
            }
        }
    }
}
