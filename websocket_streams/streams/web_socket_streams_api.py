"""
Binance Spot WebSocket Streams

OpenAPI Specifications for the Binance Spot WebSocket Streams

API documents:
  - [Github web-socket-streams documentation file](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md)
  - [General API information for web-socket-streams on website](https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams)

The version of the OpenAPI document: 1.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from typing import Optional

from ...binance_common.errors import RequiredError
from ...binance_common.utils import ws_streams_placeholder
from ...binance_common.websocket import RequestStream, WebSocketStreamBase
from ..models import (
    AggTradeResponse,
    AllMarketRollingWindowTickerResponse,
    AllMarketRollingWindowTickerWindowSizeEnum,
    AllMiniTickerResponse,
    AllTickerResponse,
    AvgPriceResponse,
    BookTickerResponse,
    DiffBookDepthResponse,
    KlineIntervalEnum,
    KlineOffsetIntervalEnum,
    KlineOffsetResponse,
    KlineResponse,
    MiniTickerResponse,
    PartialBookDepthLevelsEnum,
    PartialBookDepthResponse,
    RollingWindowTickerResponse,
    RollingWindowTickerWindowSizeEnum,
    TickerResponse,
    TradeResponse,
)


class WebSocketStreamsApi:
    """Client for WebSocketStreamsApi endpoints."""

    def __init__(self, websocket_base: WebSocketStreamBase) -> None:
        self.websocket_base = websocket_base

    async def agg_trade(
        self,
        symbol: str = None,
        id: Optional[str] = None,
    ) -> AggTradeResponse:
        r"""
        WebSocket Aggregate Trade Streams
        POST /<symbol>@aggTrade
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#aggregate-trade-streams

        The Aggregate Trade Streams push trade information that is aggregated for a single taker order.

        Args:
            symbol (str): Symbol to query
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            AggTradeResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@aggTrade".replace("/", ""),
            {
                "symbol": symbol,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=AggTradeResponse
        )

    async def all_market_rolling_window_ticker(
        self,
        window_size: AllMarketRollingWindowTickerWindowSizeEnum = None,
        id: Optional[str] = None,
    ) -> AllMarketRollingWindowTickerResponse:
        r"""
            WebSocket All Market Rolling Window Statistics Streams
            POST /!ticker_<windowSize>@arr
            https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-rolling-window-statistics-streams

            Rolling window ticker statistics for all market symbols, computed over multiple windows.
        Note that only tickers that have changed will be present in the array.

            Args:
                window_size (AllMarketRollingWindowTickerWindowSizeEnum):
                id (Optional[str]): Unique WebSocket request ID.

            Returns:
                AllMarketRollingWindowTickerResponse

            Raises:
                RequiredError: If a required parameter is missing.

        """

        if window_size is None:
            raise RequiredError(
                field="window_size",
                error_message="Missing required parameter 'window_size'",
            )

        stream = ws_streams_placeholder(
            "/!ticker_<windowSize>@arr".replace("/", ""),
            {
                "window_size": window_size,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base,
            stream=stream,
            response_model=AllMarketRollingWindowTickerResponse,
        )

    async def all_mini_ticker(
        self,
        id: Optional[str] = None,
    ) -> AllMiniTickerResponse:
        r"""
        WebSocket All Market Mini Tickers Stream
        POST /!miniTicker@arr
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-mini-tickers-stream

        24hr rolling window mini-ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

        Args:
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            AllMiniTickerResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        stream = ws_streams_placeholder(
            "/!miniTicker@arr".replace("/", ""),
            {
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=AllMiniTickerResponse
        )

    async def all_ticker(
        self,
        id: Optional[str] = None,
    ) -> AllTickerResponse:
        r"""
        WebSocket All Market Tickers Stream
        POST /!ticker@arr
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#all-market-tickers-stream

        24hr rolling window ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

        Args:
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            AllTickerResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        stream = ws_streams_placeholder(
            "/!ticker@arr".replace("/", ""),
            {
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=AllTickerResponse
        )

    async def avg_price(
        self,
        symbol: str = None,
        id: Optional[str] = None,
    ) -> AvgPriceResponse:
        r"""
        WebSocket Average Price
        POST /<symbol>@avgPrice
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#average-price

        Average price streams push changes in the average price over a fixed time interval.

        Args:
            symbol (str): Symbol to query
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            AvgPriceResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@avgPrice".replace("/", ""),
            {
                "symbol": symbol,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=AvgPriceResponse
        )

    async def book_ticker(
        self,
        symbol: str = None,
        id: Optional[str] = None,
    ) -> BookTickerResponse:
        r"""
            WebSocket Individual Symbol Book Ticker Streams
            POST /<symbol>@bookTicker
            https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-book-ticker-streams

            Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.
        Multiple `<symbol>@bookTicker` streams can be subscribed to over one connection.

            Args:
                symbol (str): Symbol to query
                id (Optional[str]): Unique WebSocket request ID.

            Returns:
                BookTickerResponse

            Raises:
                RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@bookTicker".replace("/", ""),
            {
                "symbol": symbol,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=BookTickerResponse
        )

    async def diff_book_depth(
        self,
        symbol: str = None,
        id: Optional[str] = None,
        update_speed: Optional[str] = None,
    ) -> DiffBookDepthResponse:
        r"""
        WebSocket Diff. Depth Stream
        POST /<symbol>@depth@<updateSpeed>
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#diff-depth-stream

        Order book price and quantity depth updates used to locally manage an order book.

        Args:
            symbol (str): Symbol to query
            id (Optional[str]): Unique WebSocket request ID.
            update_speed (Optional[str]): 1000ms or 100ms

        Returns:
            DiffBookDepthResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@depth@<updateSpeed>".replace("/", ""),
            {
                "symbol": symbol,
                "id": id,
                "update_speed": update_speed,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=DiffBookDepthResponse
        )

    async def kline(
        self,
        symbol: str = None,
        interval: KlineIntervalEnum = None,
        id: Optional[str] = None,
    ) -> KlineResponse:
        r"""
            WebSocket Kline/Candlestick Streams for UTC
            POST /<symbol>@kline_<interval>
            https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#klinecandlestick-streams-for-utc

            The Kline/Candlestick Stream push updates to the current klines/candlestick every second in `UTC+0` timezone

        <a id="kline-intervals"></a>

            Args:
                symbol (str): Symbol to query
                interval (KlineIntervalEnum):
                id (Optional[str]): Unique WebSocket request ID.

            Returns:
                KlineResponse

            Raises:
                RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )
        if interval is None:
            raise RequiredError(
                field="interval", error_message="Missing required parameter 'interval'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@kline_<interval>".replace("/", ""),
            {
                "symbol": symbol,
                "interval": interval,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=KlineResponse
        )

    async def kline_offset(
        self,
        symbol: str = None,
        interval: KlineOffsetIntervalEnum = None,
        id: Optional[str] = None,
    ) -> KlineOffsetResponse:
        r"""
        WebSocket Kline/Candlestick Streams with timezone offset
        POST /<symbol>@kline_<interval>@+08:00
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#klinecandlestick-streams-with-timezone-offset

        The Kline/Candlestick Stream push updates to the current klines/candlestick every second in `UTC+8` timezone

        Args:
            symbol (str): Symbol to query
            interval (KlineOffsetIntervalEnum):
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            KlineOffsetResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )
        if interval is None:
            raise RequiredError(
                field="interval", error_message="Missing required parameter 'interval'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@kline_<interval>@+08:00".replace("/", ""),
            {
                "symbol": symbol,
                "interval": interval,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=KlineOffsetResponse
        )

    async def mini_ticker(
        self,
        symbol: str = None,
        id: Optional[str] = None,
    ) -> MiniTickerResponse:
        r"""
        WebSocket Individual Symbol Mini Ticker Stream
        POST /<symbol>@miniTicker
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-mini-ticker-stream

        24hr rolling window mini-ticker statistics. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

        Args:
            symbol (str): Symbol to query
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            MiniTickerResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@miniTicker".replace("/", ""),
            {
                "symbol": symbol,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=MiniTickerResponse
        )

    async def partial_book_depth(
        self,
        symbol: str = None,
        levels: PartialBookDepthLevelsEnum = None,
        id: Optional[str] = None,
        update_speed: Optional[str] = None,
    ) -> PartialBookDepthResponse:
        r"""
        WebSocket Partial Book Depth Streams
        POST /<symbol>@depth<levels>@<updateSpeed>
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#partial-book-depth-streams

        Top **\<levels\>** bids and asks, pushed every second. Valid **\<levels\>** are 5, 10, or 20.

        Args:
            symbol (str): Symbol to query
            levels (PartialBookDepthLevelsEnum):
            id (Optional[str]): Unique WebSocket request ID.
            update_speed (Optional[str]): 1000ms or 100ms

        Returns:
            PartialBookDepthResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )
        if levels is None:
            raise RequiredError(
                field="levels", error_message="Missing required parameter 'levels'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@depth<levels>@<updateSpeed>".replace("/", ""),
            {
                "symbol": symbol,
                "levels": levels,
                "id": id,
                "update_speed": update_speed,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=PartialBookDepthResponse
        )

    async def rolling_window_ticker(
        self,
        symbol: str = None,
        window_size: RollingWindowTickerWindowSizeEnum = None,
        id: Optional[str] = None,
    ) -> RollingWindowTickerResponse:
        r"""
        WebSocket Individual Symbol Rolling Window Statistics Streams
        POST /<symbol>@ticker_<windowSize>
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-rolling-window-statistics-streams

        Rolling window ticker statistics for a single symbol, computed over multiple windows.

        Args:
            symbol (str): Symbol to query
            window_size (RollingWindowTickerWindowSizeEnum):
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            RollingWindowTickerResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )
        if window_size is None:
            raise RequiredError(
                field="window_size",
                error_message="Missing required parameter 'window_size'",
            )

        stream = ws_streams_placeholder(
            "/<symbol>@ticker_<windowSize>".replace("/", ""),
            {
                "symbol": symbol,
                "window_size": window_size,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base,
            stream=stream,
            response_model=RollingWindowTickerResponse,
        )

    async def ticker(
        self,
        symbol: str = None,
        id: Optional[str] = None,
    ) -> TickerResponse:
        r"""
        WebSocket Individual Symbol Ticker Streams
        POST /<symbol>@ticker
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#individual-symbol-ticker-streams

        24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

        Args:
            symbol (str): Symbol to query
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            TickerResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@ticker".replace("/", ""),
            {
                "symbol": symbol,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=TickerResponse
        )

    async def trade(
        self,
        symbol: str = None,
        id: Optional[str] = None,
    ) -> TradeResponse:
        r"""
        WebSocket Trade Streams
        POST /<symbol>@trade
        https://developers.binance.com/docs/binance-spot-api-docs/web-socket-streams#trade-streams

        The Trade Streams push raw trade information; each trade has a unique buyer and seller.

        Args:
            symbol (str): Symbol to query
            id (Optional[str]): Unique WebSocket request ID.

        Returns:
            TradeResponse

        Raises:
            RequiredError: If a required parameter is missing.

        """

        if symbol is None:
            raise RequiredError(
                field="symbol", error_message="Missing required parameter 'symbol'"
            )

        stream = ws_streams_placeholder(
            "/<symbol>@trade".replace("/", ""),
            {
                "symbol": symbol,
                "id": id,
            },
        )

        return await RequestStream(
            self.websocket_base, stream=stream, response_model=TradeResponse
        )
