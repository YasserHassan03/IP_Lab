module fir_filter(
  input clk,
  input reset,
  input signed [31:0] data_in,
  output signed [31:0] data_out
);

  parameter WIDTH = 32;  // word width
  parameter COEFFS [3:0] = '{1, 2, 3, 2};  // filter coefficients
  // COEFFS[0] is the coefficient for x[0], COEFFS[1] is the coefficient for x[1], and so on
  //also add memory initialisation code to read the data from the accelerometer (SPI/12C etc)
  //specify address width,coefficient width and memory depth in hardware use block in an fpga
  
  reg signed [WIDTH-1:0] x [0:3];  // input shift register
  wire signed [WIDTH-1:0] y;       // filter output

  assign data_out = y;  // output the filtered data

  always @(posedge clk) begin
    if (reset) begin
      // reset the input shift register
      x <= {WIDTH{1'b0}};
    end else begin
      // shift the input data into the shift register
      x[0] <= data_in;
      x[1] <= x[0];
      x[2] <= x[1];
      x[3] <= x[2];
    end
  end

  assign y = 0;
  // Sum the products of the filter coefficients and the values in the input shift register taps using a for loop
  for (int i = 0; i < COEFFS.size(); i++) begin
    y = y + COEFFS[i] * x[i];
  end

endmodule
