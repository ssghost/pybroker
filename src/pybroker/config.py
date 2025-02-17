"""Contains configuration options."""

"""Copyright (C) 2023 Edward West

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from .common import BarData, FeeMode, PriceType
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Callable, Optional, Union


@dataclass(frozen=True)
class StrategyConfig:
    """Configuration options for :class:`pybroker.strategy.Strategy`.

    Attributes:
        initial_cash: Starting cash of strategy.
        fee_mode: :class:`pybroker.common.FeeMode` for calculating brokerage
            fees. Supports one of:

            - ``ORDER_PERCENT``: Fee is a percentage of order amount.
            - ``PER_ORDER``: Fee is a constant amount per order.
            - ``PER_SHARE``: Fee is a constant amount per share in order.
            - ``None``: Fees are disabled (default).
        fee_amount: Brokerage fee amount.
        enable_fractional_shares: Whether to enable trading fractional shares.
            Set to ``True`` for crypto trading. Defaults to ``False``.
        max_long_positions: Maximum number of long positions that can be held
            at any time in :class:`pybroker.portfolio.Portfolio`. Unlimited
            when ``None``. Defaults to ``None``.
        max_short_positions: Maximum number of short positions that can be
            held at any time in :class:`pybroker.portfolio.Portfolio`.
            Unlimited when ``None``. Defaults to ``None``.
        buy_delay: Number of bars before placing an order for a buy signal. The
            default value of ``1`` places a buy order on the next bar. Must be
            > ``0``.
        sell_delay: Number of bars before placing an order for a sell signal.
            The default value of ``1`` places a sell order on the next bar.
            Must be > ``0``.
        bootstrap_samples: Number of samples used to compute boostrap metrics.
            Defaults to ``10_000``.
        bootstrap_sample_size: Size of each random sample used to compute
            bootstrap metrics. Defaults to ``1_000``.
        exit_on_last_bar: Whether to automatically exit any open positions
            on the last bar of data available for a symbol. Defaults to
            ``False``.
        exit_cover_fill_price: Fill price for covering an open short position
            when :attr:`.exit_on_last_bar` is ``True``. Defaults to
            :attr:`pybroker.common.PriceType.MIDDLE`.
        exit_sell_fill_price: Fill price for selling an open long position when
            :attr:`.exit_on_last_bar` is ``True``. Defaults to
            :attr:`pybroker.common.PriceType.MIDDLE`.
        sharpe_length: Number of observations used to annualize the Sharpe
            Ratio. For example, a value of ``252`` would be used to annualize
            daily returns.
    """

    initial_cash: float = field(default=100_000)
    fee_mode: Optional[FeeMode] = field(default=None)
    fee_amount: float = field(default=0)
    enable_fractional_shares: bool = field(default=False)
    max_long_positions: Optional[int] = field(default=None)
    max_short_positions: Optional[int] = field(default=None)
    buy_delay: int = field(default=1)
    sell_delay: int = field(default=1)
    bootstrap_samples: int = field(default=10_000)
    bootstrap_sample_size: int = field(default=1_000)
    exit_on_last_bar: bool = field(default=False)
    exit_cover_fill_price: Union[
        PriceType, Callable[[str, BarData], Union[int, float, Decimal]]
    ] = field(default=PriceType.MIDDLE)
    exit_sell_fill_price: Union[
        PriceType, Callable[[str, BarData], Union[int, float, Decimal]]
    ] = field(default=PriceType.MIDDLE)
    sharpe_length: Optional[int] = field(default=None)
