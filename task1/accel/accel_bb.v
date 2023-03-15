
module accel (
	accelerometer_spi_external_interface_I2C_SDAT,
	accelerometer_spi_external_interface_I2C_SCLK,
	accelerometer_spi_external_interface_G_SENSOR_CS_N,
	accelerometer_spi_external_interface_G_SENSOR_INT,
	clk_clk,
	hex_0_export,
	hex_1_export,
	hex_2_export,
	hex_3_export,
	hex_4_export,
	hex_5_export,
	led_external_connection_export,
	reset_reset_n);	

	inout		accelerometer_spi_external_interface_I2C_SDAT;
	output		accelerometer_spi_external_interface_I2C_SCLK;
	output		accelerometer_spi_external_interface_G_SENSOR_CS_N;
	input		accelerometer_spi_external_interface_G_SENSOR_INT;
	input		clk_clk;
	output	[6:0]	hex_0_export;
	output	[6:0]	hex_1_export;
	output	[6:0]	hex_2_export;
	output	[6:0]	hex_3_export;
	output	[6:0]	hex_4_export;
	output	[6:0]	hex_5_export;
	output	[9:0]	led_external_connection_export;
	input		reset_reset_n;
endmodule
